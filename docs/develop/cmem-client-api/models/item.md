# `item` {#cmem_client.models.item}

ImportItem base class and inherited classes

A marketplace package can be installed from a directory, a single file or a zip
archive. These classes hide that difference: ``create_import_item()`` picks the right
one for a path, and using it as a context manager yields a directory the import can
read from, extracting the archive first where that is needed and cleaning up after.

**Classes:**

- [**DirectoryImportItem**](#cmem_client.models.item.DirectoryImportItem) – Import from a directory - no transformation needed.
- [**FileImportItem**](#cmem_client.models.item.FileImportItem) – Import from a single file, copy to temp directory.
- [**ImportItem**](#cmem_client.models.item.ImportItem) – Abstract base class for different import source types.
- [**ZipImportItem**](#cmem_client.models.item.ZipImportItem) – Import from a zip archive - extract to temp directory.

**Functions:**

- [**create_import_item**](#cmem_client.models.item.create_import_item) – Factory function to create appropriate ImportItem instance.

## `DirectoryImportItem` {#cmem_client.models.item.DirectoryImportItem}

Bases: <code>[ImportItem](#cmem_client.models.item.ImportItem)</code>

Import from a directory - no transformation needed.

**Functions:**

- [**cleanup**](#cmem_client.models.item.DirectoryImportItem.cleanup) – No cleanup needed for directories.
- [**detect**](#cmem_client.models.item.DirectoryImportItem.detect) – Detect the appropriate ImportItem type for the given source.
- [**prepare**](#cmem_client.models.item.DirectoryImportItem.prepare) – Return directory path as-is.

**Attributes:**

- [**import_type**](#cmem_client.models.item.DirectoryImportItem.import_type) – 
- [**model_config**](#cmem_client.models.item.DirectoryImportItem.model_config) – 
- [**source**](#cmem_client.models.item.DirectoryImportItem.source) – 

### `cleanup` {#cmem_client.models.item.DirectoryImportItem.cleanup}

```python
cleanup()
```

No cleanup needed for directories.

### `detect` {#cmem_client.models.item.DirectoryImportItem.detect}

```python
detect(source)
```

Detect the appropriate ImportItem type for the given source.

**Parameters:**

- **source** (<code>Path</code>) – Path to analyze

**Returns:**

- <code>type[[ImportItem](#cmem_client.models.item.ImportItem)]</code> – The appropriate ImportItem subclass

### `import_type` {#cmem_client.models.item.DirectoryImportItem.import_type}

```python
import_type = 'directory'
```

### `model_config` {#cmem_client.models.item.DirectoryImportItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `prepare` {#cmem_client.models.item.DirectoryImportItem.prepare}

```python
prepare()
```

Return directory path as-is.

### `source` {#cmem_client.models.item.DirectoryImportItem.source}

```python
source = Path(source) if isinstance(source, str) else source
```

## `FileImportItem` {#cmem_client.models.item.FileImportItem}

Bases: <code>[ImportItem](#cmem_client.models.item.ImportItem)</code>

Import from a single file, copy to temp directory.

**Functions:**

- [**cleanup**](#cmem_client.models.item.FileImportItem.cleanup) – Remove temporary directory.
- [**detect**](#cmem_client.models.item.FileImportItem.detect) – Detect the appropriate ImportItem type for the given source.
- [**prepare**](#cmem_client.models.item.FileImportItem.prepare) – Copy file to a temporary directory.

**Attributes:**

- [**import_type**](#cmem_client.models.item.FileImportItem.import_type) – 
- [**model_config**](#cmem_client.models.item.FileImportItem.model_config) – 
- [**source**](#cmem_client.models.item.FileImportItem.source) – 

### `cleanup` {#cmem_client.models.item.FileImportItem.cleanup}

```python
cleanup()
```

Remove temporary directory.

### `detect` {#cmem_client.models.item.FileImportItem.detect}

```python
detect(source)
```

Detect the appropriate ImportItem type for the given source.

**Parameters:**

- **source** (<code>Path</code>) – Path to analyze

**Returns:**

- <code>type[[ImportItem](#cmem_client.models.item.ImportItem)]</code> – The appropriate ImportItem subclass

### `import_type` {#cmem_client.models.item.FileImportItem.import_type}

```python
import_type = 'file'
```

### `model_config` {#cmem_client.models.item.FileImportItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `prepare` {#cmem_client.models.item.FileImportItem.prepare}

```python
prepare()
```

Copy file to a temporary directory.

### `source` {#cmem_client.models.item.FileImportItem.source}

```python
source = Path(source) if isinstance(source, str) else source
```

## `ImportItem` {#cmem_client.models.item.ImportItem}

```python
ImportItem(source)
```

Bases: <code>ABC</code>, <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Abstract base class for different import source types.

Each concrete implementation represents a different source type
(file, directory, zip, etc.) and knows how to prepare itself
for import by providing a Path to a directory or file.

**Attributes:**

- [**import_type**](#cmem_client.models.item.ImportItem.import_type) (<code>str</code>) – Name of the source type this class handles, one of ``directory``,
``file`` or ``zip``.
- [**source**](#cmem_client.models.item.ImportItem.source) – Path the import reads from, as passed to the constructor.

**Functions:**

- [**cleanup**](#cmem_client.models.item.ImportItem.cleanup) – Clean up any temporary resources created during preparation.
- [**detect**](#cmem_client.models.item.ImportItem.detect) – Detect the appropriate ImportItem type for the given source.
- [**prepare**](#cmem_client.models.item.ImportItem.prepare) – Prepare the import source and return a path to import from.

**Parameters:**

- **source** (<code>Path | str</code>) – Source path or identifier for the import

### `cleanup` {#cmem_client.models.item.ImportItem.cleanup}

```python
cleanup()
```

Clean up any temporary resources created during preparation.

### `detect` {#cmem_client.models.item.ImportItem.detect}

```python
detect(source)
```

Detect the appropriate ImportItem type for the given source.

**Parameters:**

- **source** (<code>Path</code>) – Path to analyze

**Returns:**

- <code>type[[ImportItem](#cmem_client.models.item.ImportItem)]</code> – The appropriate ImportItem subclass

### `import_type` {#cmem_client.models.item.ImportItem.import_type}

```python
import_type: str
```

### `model_config` {#cmem_client.models.item.ImportItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `prepare` {#cmem_client.models.item.ImportItem.prepare}

```python
prepare()
```

Prepare the import source and return a path to import from.

This method transforms the source into a format suitable for import.
For example:
- Zip files are extracted to a temp directory
- Directories are returned as-is

**Returns:**

- <code>Path</code> – Path to directory or file ready for import

### `source` {#cmem_client.models.item.ImportItem.source}

```python
source = Path(source) if isinstance(source, str) else source
```

## `ZipImportItem` {#cmem_client.models.item.ZipImportItem}

```python
ZipImportItem(source)
```

Bases: <code>[ImportItem](#cmem_client.models.item.ImportItem)</code>

Import from a zip archive - extract to temp directory.

**Functions:**

- [**cleanup**](#cmem_client.models.item.ZipImportItem.cleanup) – Remove temporary directory.
- [**detect**](#cmem_client.models.item.ZipImportItem.detect) – Detect the appropriate ImportItem type for the given source.
- [**prepare**](#cmem_client.models.item.ZipImportItem.prepare) – Extract zip to temporary directory.

**Attributes:**

- [**import_type**](#cmem_client.models.item.ZipImportItem.import_type) – 
- [**model_config**](#cmem_client.models.item.ZipImportItem.model_config) – 
- [**source**](#cmem_client.models.item.ZipImportItem.source) – 

### `cleanup` {#cmem_client.models.item.ZipImportItem.cleanup}

```python
cleanup()
```

Remove temporary directory.

### `detect` {#cmem_client.models.item.ZipImportItem.detect}

```python
detect(source)
```

Detect the appropriate ImportItem type for the given source.

**Parameters:**

- **source** (<code>Path</code>) – Path to analyze

**Returns:**

- <code>type[[ImportItem](#cmem_client.models.item.ImportItem)]</code> – The appropriate ImportItem subclass

### `import_type` {#cmem_client.models.item.ZipImportItem.import_type}

```python
import_type = 'zip'
```

### `model_config` {#cmem_client.models.item.ZipImportItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `prepare` {#cmem_client.models.item.ZipImportItem.prepare}

```python
prepare()
```

Extract zip to temporary directory.

### `source` {#cmem_client.models.item.ZipImportItem.source}

```python
source = Path(source) if isinstance(source, str) else source
```

## `create_import_item` {#cmem_client.models.item.create_import_item}

```python
create_import_item(source)
```

Factory function to create appropriate ImportItem instance.

**Parameters:**

- **source** (<code>Path</code>) – Path to the import source

**Returns:**

- <code>[ImportItem](#cmem_client.models.item.ImportItem)</code> – Appropriate ImportItem instance based on source type

