# pack

Pack images into one big texture Atlas.
The pack algorithm will try to fit all
provided images into the defined rectangle. The command fails of not all images fit.
## Usage

`woogac pack [FLAGS] [OPTIONS] [Files]...`

## Flags

| name              | description                                           |
| ----------------- | ----------------------------------------------------- |
| `-f`, `--force`   | Prints help information                               |
| `-h`, `--help`    | Prints help information                               |
| `-V`, `--version` | Prints version information                            |

## Options

| name                              | description                 | default value | possible values           | env                      |
| --------------------------------- | --------------------------- | ------------- | ------------------------- | ------------------------ |
| `-o`, `--output-dir <Dir>`       | Output directory to use. This argument must point to a valid writable directory. | - | - | `PWD`    |
| `--format <format>` | output file format | `png` | `png`, `jpg` | `WOOGAC_RESIZE_FORMAT` |
| `-h`,<br/> `--height <height>` | Height of the texture atlas. This value determines the final height of the texture atlas. | `2048` | - | - |
| `-w`,<br/> `--width <width>` | Width of the texture atlas. This value determines the final width of the texture atlas. | `2048` | - | - |
| `--file-name <file_name>`        | The file name of for the texture atlas without extension | `texture_atlas`  | -                         | `WOOGAC_PACK_FILENAME` |

## ARGS

| name         | description                         |
| ------------ | ----------------------------------- |
| `<FILES>...` | Input file[s] to pack. One or more file paths to valid image files. Files must be files and not directories. |

## Examples

Here are a few examples to show some basic use cases

#### pack provided images into the texture atlas

`woogac pack image1.png image2.png image3.png image4.png image5.png`

This will create two files in the working directory. A texture atlas named `texture_atlas.png` and the atlas manifest in json format `texture_atlas.json`

#### pack provided images into the texture atlas as with jpg format

`woogac pack --format jpg image1.png image2.png image3.png image4.png image5.png`

This will create two files in the working directory. A texture atlas named `texture_atlas.jpg`

#### export atlas to a different directory

`woogac pack --output-dir export/path image1.png image2.png image3.png image4.png image5.png`

This exports both texture atlas and manifest to the provided directory `export/path`. The directory must exist before executing.

#### set filename for exported atlas

`woogac pack --file-name atlas1 image1.png image2.png image3.png image4.png image5.png`

Both texture atlas and manifest will be named according to the provided name `atlas1.png`/`atlas1.json`

#### set custom atlas width and height

`woogac pack --width 4096 --height 512 image1.png image2.png image3.png image4.png image5.png`
