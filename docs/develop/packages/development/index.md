---
title: "Marketplace Package Development"
icon: material/code-json
tags:
    - Marketplace
    - Package
---
# Marketplace Package Development

## Introduction

In order to support the development of packages, we published a [package template](https://github.com/eccenca/cmem-package-template).
Please have a look at this project to get started.

This page walks you through a basic example of creating a new package, adding different type of content inside it and finally building it into a package archive ready for distribution.

## Creating your own package

## Initializing

Using [described instructions](https://github.com/eccenca/cmem-package-template/tree/main#usage) have a local folder contain your newly templated project (`my-package-id`), for our example we will use :
```shell
🎤 Type of package
   Project Package
🎤 Package ID (e.g., 'eccenca-supply-chain-vocab', 'w3c-org-vocab')
   my-package-id
🎤 Human-readable package name (e.g., 'My Awesome Vocabulary', 'My Great Project' ..)
   My own package
🎤 Short description of the package (e.g., 'A vocabulary for ...', 'A project ...')
   My project and graphs
```

You should now have a folder with two level of files :

- Top level — generic package information such as the changelog, README, CI instructions, and licensing.
- Nested folder (my-package-id) — the actual package content, along with a manifest.

## Package content

The nested folder `my-package-id` represents your working directory for developing the package.

To add content to the package simply drag and drop files you want added into this folder or extract existing content from a live Corporate Memory instance to the working directory.

!!! Example "Extracting Corporate Memory content to add to the package "

    ```shell
    cmemc graph export https://my-company.org/queries/ --output-file my-package-id/queries.ttl

    cmemc project export MyProject_78e981443900a761 --output-dir my-package-id
    Export project 1/1: MyProject_78e981443900a761 to my-package-id/2026-07-08-unnamed-MyProject_78e981443900a761.project.zip ... done

    mv my-package-id/2026-07-08-unnamed-MyProject_78e981443900a761.project.zip my-package-id/project.zip
    ```

## Declaring the files in the manifest

In order for the package to know about these added files, the `cpa-manifest.json` needs to be edited.

The `"files":[]` section of the manifest references the files the package needs to bundle.
Complete information about the [package manifest can be found here](https://github.com/eccenca/cmem-package-template/tree/main#package-manifest) and more specifically [how to declare new files](https://github.com/eccenca/cmem-package-template/tree/main#adding-files).

For our example we will be adding a query graph and a project file, make sure you use valid `file_path` relative to your package working directory (nested folder).

### Adding graph and project

```json
"files": [
  {...},
  {
    "file_path": "queries.ttl", // inside my-package-id nested folder
    "file_type": "graph",
    "graph_iri": "https://my-company.org/queries/",
    "import_into": [],
     "register_as_vocabulary": false
  },
  {
    "file_path": "project.zip", // inside my-package-id nested folder
    "file_type": "project",
    "project_id": "MyProject_78e981443900a761"
  }
]
```

## Testing your package

To ensure the package correctly detects your added files, you can try to import it in a Corporate Memory instance.

The package template comes with a predefined `Taskfile.yaml` allowing you to wrap your development steps in single commands.
```shell
task: Available tasks for this project:
* build:         Build package archive
* check:         Run whole test suite
* clean:         Removes dist, *.cpa, ...
* delete:        Delete (uninstall) package from Corporate Memory
* export:        Export package content from Corporate Memory
* import:        Import (install) package to Corporate Memory
* publish:       Publish package archive to the marketplace
```

To tell the package system to take files from the local working directory and to import them inside Corporate Memory we use **task import**.
An import will always try to uninstall previously installed version of the same package, to ensure it is correctly replaced.

```shell
task import
task: [delete] cmemc package uninstall $package_id
Package 'my-package-id' is not installed.
task: [import] cmemc package install --input $package_dir
Installing package 'my-package-id' from 'my-package-id' ... done
```

!!! Warning "Importing duplicated content"

    If you extracted from Corporate Memory already existing content and added it to your package with the same identifiers (graph URIs, projects IDs, ...), and try to import it back in the form of a new package, the instance might raise a `MarketplacePackagesImportError` due to conflicting elements : (Repository item 'https://my-company.org/queries/' already exists.) .

    In this case, you can simply delete your duplicated content inside Corporate Memory (make sure you do backups in case) before importing them back as a package content.
    The difference will be that now Corporate Memory will know this content is part of a managed package, and will handle import/export on that file from now on.

## Updating the package file content

If you make modifications to your package content in Corporate Memory, the files will not automatically sync back with your local working directory.

To extract all the updated content from Corporate Memory into your package working directory in a managed way, simply run **task export**

```shell
task export
```

!!! Warning "Exporting without installing first"

    The platform can only export updated versions of package files that were imported at least once before. If you create new information directly in Corporate Memory that the package manifest doesn't yet declare, such as new graphs, you need to manually add them to your working directory and to your manifest and then import them.

    The rule of thumb is : if you need to make structural change to your package that requires for you to edit your manifest, then make sure to run `import` right after to let Corporate Memory keep track of new files.

    Adding a workflow inside a project is not impacted by this limitation, since it is part of the "project" that is managed and tracked by the package.

## Building your package

To generate a `.cpa` file ready to be distributed and installed in different Corporate Memory instances you can run **task build**.

Make sure your local package folder is a git repository with a clean state (the commit hash is used to generate the cpa).
```shell
task build
```

To check how this output `.cpa` file can be imported in different places refer to the [Installation and Usage section](../installation/index.md).

!!! Success "Next steps"

    There are many improvements you can add to your package, such as declaring dependencies to other plugins or packages, to ensure your `.cpa` file can be installed with all it's requirements everywhere, for that you can refer to existing package examples or the template documentation.

    The final step is usually publishing a version of the package to a remote Marketplace repository, to avoid having to manually transfert the `.cpa` archive. This requires you to have publishing permissions on an eccenca Marketplace instance (either a public or private instance).
    This can be done with task publish, either manually or from a CI runner.
