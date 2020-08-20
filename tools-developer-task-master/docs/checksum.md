# checksum

calculates sha256 checksums for provided file[s].

## Usage

`woogac checksum [OPTIONS] [Files]...`

## Flags

| name              | description                                           |
| ----------------- | ----------------------------------------------------- |
| `-h`, `--help`    | Prints help information                               |
| `-V`, `--version` | Prints version information                            |

## Options

| name                              | description                 | default value | possible values           | env                      |
| --------------------------------- | --------------------------- | ------------- | ------------------------- | ------------------------ |
| `--file-name <file_name>`         | The file name for the report. The default name depends on the selected `--output-format`. | `checksums.txt` / `checksums.json`  | - | `WOOGAC_CHECKSUM_FILENAME` |
| `-o`,<br/> `--output-dir <Dir>`   | Output directory to use. This argument must point to a valid writable directory The report will be written to stdout, if this option is not provided. | - | - | - |
| `--output-format <output-format>` | The output format. The format is either plain text file. Each line contains the file path and the checksum seperated by a space character. Or a json hashmap"| `plain` | `json`, `plain` | `WOOGAC_CHECKSUM_OUTPUT_FORMAT` |


## ARGS

| name         | description                         |
| ------------ | ----------------------------------- |
| `<FILES>...` | input file[s] generate checksum for |

## Examples

Here are a few examples to show some basic use cases

#### output sha256 checksum info for a single file

`woogac checksum file.txt`

This will print the path and sha256 checksum of the provided file

```plain
/path/to/file.txt 5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144
```

#### output sha256 checksum for a multiple files

`woogac checksum file1.txt file2.txt`

This will print the path and sha256 checksum of the provided files. One file per line

```plain
/path/to/file1.txt 5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144
/path/to/file2.txt 884b32c07ee64f1acbd0e6bd6d63d0e8784146325f08464fcd29fe2d3adf04f1
```

#### output sha256 checksum info for a single file in json format

`woogac checksum --output-format json file.txt`

This will print the path and sha256 checksum of the provided image as a json hash

```json
{
  "/path/to/file.txt": "5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144"
}
```

#### output sha256 checksum info for multiple files in json format

`woogac checksum --output-format json file1.txt file2.txt`

This will print the path and sha256 checksum of the provided files as a json hash

```json
{
  "/path/to/file1.png": "5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144",
  "/path/to/file2.png": "884b32c07ee64f1acbd0e6bd6d63d0e8784146325f08464fcd29fe2d3adf04f1"
}
```

#### redirect output to directory

`woogac checksum --output-dir . file.txt`

Saves the output in a file. By default the filename will be either `info.txt` or `info.json` depending on the selected `--output-format`.

#### redirect output from multiple files to directory with custom filename

`woogac checksum --output-dir . --file-name custom-info.txt file1.txt file2.txt`
