---
title: "Marketplace Packages: Development Tutorial"
icon: material/school
tags:
    - Marketplace
    - Package
---
# Tutorial: Develop your first Marketplace Package

This tutorial walks you through a basic example of creating a new Marketplace Package, adding different types of content to it, and finally building it into a package archive ready for distribution.

It is a "how to" and does not replace the full documentation of the [package-template](https://github.com/eccenca/cmem-package-template) repository.
See [Development and Publication](index.md) for the underlying concepts, and note that advanced scenarios such as publishing are only outlined at the end.

## Initialize the Package Repository

Follow the [template usage instructions](https://github.com/eccenca/cmem-package-template/tree/main#usage) to create a local package repository.
For our example, we answer the template questions as follows:

```shell title="copier copy gh:eccenca/cmem-package-template my-package-id"
🎤 Type of package
   Project Package
🎤 Package ID (e.g., 'eccenca-supply-chain-vocab', 'w3c-org-vocab')
   my-package-id
🎤 Human-readable package name (e.g., 'My Awesome Vocabulary', 'My Great Project')
   My own package
🎤 Short description of the package (e.g., 'A vocabulary for ...', 'A project that ...')
   My project and graphs
🎤 Comma-separated Python package dependencies (e.g., 'cmem-plugin-pyshacl, cmem-plugin-llm')

🎤 Comma-separated vocabulary or project dependencies (e.g., 'aksw-rut-vocab, my-other-project')

🎤 github_page: This URL (e.g. https://github.com/user/repo) will be used as the base for icons and the homepage link. Leave blank if your package is not on github.

```

You should now have a folder with two levels of files:

- Top level - generic package repository information such as the changelog, README, CI instructions, licensing, and the `Taskfile.yaml`.
- Nested folder (`my-package-id`) - the package directory holding the actual package content, along with the `cpa-manifest.json` manifest.

## Add Package Content

The nested folder `my-package-id` represents your working directory for developing the package.

To add content to the package, simply copy the files you want to add into this folder, or extract existing content from a live Corporate Memory instance into the working directory.

!!! example "Extracting Corporate Memory content to add to the package"

    ```shell
    cmemc graph export https://my-company.org/queries/ --output-file my-package-id/queries.ttl

    cmemc project export MyProject_78e981443900a761 --output-dir my-package-id
    Export project 1/1: MyProject_78e981443900a761 to my-package-id/2026-07-08-unnamed-MyProject_78e981443900a761.project.zip ... done

    mv my-package-id/2026-07-08-unnamed-MyProject_78e981443900a761.project.zip my-package-id/project.zip
    ```

## Declare the Files in the Manifest

In order for the package to know about these added files, the `cpa-manifest.json` needs to be edited.

The `"files": []` section of the manifest references the files the package needs to bundle.
Complete information about the [package manifest can be found here](https://github.com/eccenca/cmem-package-template/tree/main#package-manifest), and more specifically [how to declare new files](https://github.com/eccenca/cmem-package-template/tree/main#adding-files).

For our example, we add a query graph and a project file.
Make sure each `file_path` is valid and relative to your package directory (the nested folder):

```json title="my-package-id/cpa-manifest.json"
"files": [
  {…},
  {
    "file_path": "queries.ttl",
    "file_type": "graph",
    "graph_iri": "https://my-company.org/queries/",
    "import_into": [],
    "register_as_vocabulary": false
  },
  {
    "file_path": "project.zip",
    "file_type": "project",
    "project_id": "MyProject_78e981443900a761"
  }
]
```

## Test your Package

To ensure the package correctly detects your added files, you can try to import it into a Corporate Memory instance.

The package template comes with a predefined `Taskfile.yaml` allowing you to wrap your development steps in single commands:

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

To tell the package system to take files from the local working directory and to import them into Corporate Memory, we use **task import**.
An import always tries to uninstall a previously installed version of the same package first, to ensure it is correctly replaced.

```shell
task import
task: [delete] cmemc package uninstall $package_id
Package 'my-package-id' is not installed.
task: [import] cmemc package install --input $package_dir
Installing package 'my-package-id' from 'my-package-id' ... done
```

!!! warning "Importing duplicated content"

    If you extracted already existing content from Corporate Memory, added it to your package with the same identifiers (graph IRIs, project IDs, ...), and try to import it back in the form of a new package, the instance might raise a `MarketplacePackagesImportError` due to conflicting elements, e.g. `Repository item 'https://my-company.org/queries/' already exists.`

    In this case, you can simply delete the duplicated content inside Corporate Memory (make sure you have backups) before importing it back as package content.
    The difference is that Corporate Memory now knows this content is part of a managed package, and will handle import/export of that file from now on.

## Update the Package File Content

If you make modifications to your package content in Corporate Memory, the files will not automatically sync back to your local working directory.

To extract all updated content from Corporate Memory into your package working directory in a managed way, simply run **task export**:

```shell
task export
```

!!! warning "Exporting without installing first"

    The platform can only export updated versions of package files that were imported at least once before. If you create new information directly in Corporate Memory that the package manifest does not yet declare, such as new graphs, you need to manually add them to your working directory and to your manifest, and then import them.

    The rule of thumb is: if you need to make a structural change to your package that requires you to edit your manifest, then make sure to run `import` right after, to let Corporate Memory keep track of new files.

    Adding a workflow inside a project is not impacted by this limitation, since it is part of the "project" that is managed and tracked by the package.

## Build your Package

To generate a `.cpa` file ready to be distributed and installed in different Corporate Memory instances, you can run **task build**.

Make sure your local package folder is a git repository with a clean state - the task derives the package version from `git describe`, so the commit hash ends up in the archive name (e.g. `my-package-id-v0.0.0-4b7516f.cpa`).

```shell
task build
```

To check how this output `.cpa` file can be installed in different places, refer to the [Installation and Management](../installation/index.md) section.

!!! success "Next steps"

    There are many improvements you can add to your package, such as declaring dependencies to other plugins or packages, to ensure your `.cpa` file can be installed with all its requirements everywhere. For that, you can refer to existing package examples, the [Development and Publication](index.md) page, or the template documentation.

    The final step is usually publishing a version of the package to a remote Marketplace Server, to avoid having to transfer the `.cpa` archive manually. This requires you to have publishing permissions on an eccenca Marketplace Server (either a public or private instance).
    This can be done with **task publish**, either manually or from a CI runner.
