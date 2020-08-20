# resize

Resize a set of image files.
This command allows to batch resize images.

## Usage

`woogac resize [FLAGS] [OPTIONS] <Files>...`

## Flags

| name              | description                                           |
| ----------------- | ----------------------------------------------------- |
| `--exact`         | Resize without preserving aspect ratio                |
| `-f`, `--force`   | Prints help information                               |
| `-h`, `--help`    | Prints help information                               |
| `-V`, `--version` | Prints version information                            |
| `--use-percent`   | Interpret width and height argument as percentage values. When this flag is set, Both `--with` and `--height` arguments will be interpreted as percent values. This allows to increase a series of images by the same factor. If `--use-percent` is set `--exact` is not set, then only one argument for `--width` or `--height` is needed.                           |

## Options

| name                              | description                 | default value | possible values           | env                      |
| --------------------------------- | --------------------------- | ------------- | ------------------------- | ------------------------ |
| `-o`, `--output-dir <Dir>`       | Output directory to use. This argument must point to a valid writable directory. | - | - | `PWD`    |
| `--format <format>` | output file format | `png` | `png`, `jpg` | `WOOGAC_RESIZE_FORMAT` |
| `-h`,<br/> `--height <height>` | Target height to resize image to. By default the resize is preserving the aspect ratio of the provided image. If the `--exact` flag is also set, then the command will resize the image exactly to the provided height. If this argument is not provided, the current image height will be used. If the `--percent` flag is set, the value will be interpreted as a percentage value. If this argument is not provided but the `--percent` flag is set the, the value 100 will be used. | - | - | - |
| `-w`,<br/> `--width <width>` | Target width to resize image to. By default the resize is preserving the aspect ratio of the provided image. If the `--exact` flag is also set, then the command will resize the image exactly to the provided width. If this argument is not provided, the current image width will be used. If the `--percent` flag is set, the value will be interpreted as a percentage value. If this argument is not provided but the `--percent` flag is set the, the value 100 will be used. | - | - | - |
| `-p`<br/>, `--name-pattern <name_pattern>` | A name pattern to use for the output file. Each provided image file will be renamed according to this pattern. The command uses two variables which can be used to control the final file name:<br/>* `{name}`: the original file name without file extension<br/>* `{ext}`: the new file extension based on the provided `--format` | `{name}.{ext}` | - | `WOOGAC_RESIZE_NAME_PATTERN` |
| `--output-format <output-format>` | The output format. The format is either plain text file. Each line contains the `file-path` `width` and `height` and the `checksum` separated by a space character. Or a json hashmap| `plain` | `json`, `plain` | `WOOGAC_RESIZE_OUTPUT_FORMAT` |


## ARGS

| name         | description                         |
| ------------ | ----------------------------------- |
| `<FILES>...` | Input file[s] to resize. One or more file paths to valid image files. Files must be files and not directories. |

## Examples

Here are a few examples to show some basic use cases

#### resize image proportional to 40px by 80px with the default format

`woogac resize --width 40 --height 80 image.png`

#### resize multiple images proportional to 40px by 80px with the to jpg format

`woogac resize --width 40 --height 80 --format jpg image1.png image2.png`

#### save images in different directory after resize

`woogac resize --width 20 --height 20 --output-dir export image1.png image2.png`

#### rename images with pattern

`woogac resize --width 20 --height 20 --name-patter '{name}_sm.{ext}' image1.png image2.png`

#### change report output format to json

`woogac resize --width 20 --output-format json image1.png`

#### resize image to exact width and height values

`woogac resize --exact --width 20 --height 20  image1.png`

#### resize with percentage values

`woogac resize --use-percent --width 20 --height 20  image1.png`

#### force override of existing files

`woogac resize --force --width 20 --height 20  image1.png`
