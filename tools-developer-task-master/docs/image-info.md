# image-info

reads image informations for provided file[s].

## Usage

`woogac image-info [OPTIONS] [Files]...`

## Flags

| name              | description                                           |
| ----------------- | ----------------------------------------------------- |
| `-h`, `--help`    | Prints help information                               |
| `-V`, `--version` | Prints version information                            |

## Options

| name                              | description                 | default value | possible values           | env                      |
| --------------------------------- | --------------------------- | ------------- | ------------------------- | ------------------------ |
| `--file-name <file_name>`         | The file name for the report. The default name depends on the selected `--output-format`. | `info.txt` / `info.json`  | - | `WOOGAC_IMAGE_INFO_FILENAME` |
| `-o`,<br/> `--output-dir <Dir>`   | Output directory to use. This argument must point to a valid writable directory The report will be written to stdout, if this option is not provided. | - | - | - |
| `--output-format <output-format>` | The output format. The format is either plain text file. Each line contains the `file-path` `width` and `height` and the `checksum` separated by a space character. Or a json hashmap| `plain` | `json`, `plain` | `WOOGAC_IMAGE_INFO_OUTPUT_FORMAT` |


## ARGS

| name         | description                         |
| ------------ | ----------------------------------- |
| `<FILES>...` | Input file[s] to fetch information for. One or more file paths to valid image files. Files must be files and not directories. |

## Examples

Here are a few examples to show some basic use cases

#### output image info for a single image

`woogac image-info image.png`

This will print the path, width and height and sha256 checksum of the provided image

```plain
/path/to/image.png 62 33 5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144
```

#### output image info for multiple images

`woogac image-info image1.png image2.png`

This will print the path, width and height and sha256 checksum of the provided images. One image per line

```plain
/path/to/image1.png 62 33 5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144
/path/to/image2.png 40 60 884b32c07ee64f1acbd0e6bd6d63d0e8784146325f08464fcd29fe2d3adf04f1
```

#### output image info for a single image in json format

`woogac image-info --output-format json image.png`

This will print the path, width and height and sha256 checksum of the provided image as a json hash

```json
{
  "/path/to/image.png": {
    "size": {
      "width": 62,
      "height": 33
    },
    "checksum": "5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144"
  }
}
```

#### output image info for multiple images in json format

`woogac image-info --output-format json image1.png image2.png`

This will print the path, width and height and sha256 checksum of the provided images as a json hash

```json
{
  "/path/to/image1.png": {
    "size": {
      "width": 62,
      "height": 33
    },
    "checksum": "5488521a9dfe1bad31164609d018fcd645a263c9e3108fd79823f3389628a144"
  },
  "/path/to/image2.png": {
    "size": {
      "width": 40,
      "height": 60
    },
    "checksum": "884b32c07ee64f1acbd0e6bd6d63d0e8784146325f08464fcd29fe2d3adf04f1"
  }
}
```

#### redirect output to directory

`woogac image-info --output-dir . image.png`

Saves the output in a file. By default the filename will be either `info.txt` or `info.json` depending on the selected `--output-format`.

#### redirect output from multiple images to directory with custom filename

`woogac image-info --output-dir . --file-name custom-info.txt image1.png image2.png`
