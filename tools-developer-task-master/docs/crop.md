# crop

Crop image[s] from center with provided width and height.

## Usage

`woogac crop [FLAGS] [OPTIONS] --height <height> --width <width> [Files]...`

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
| `--format <format>` | output file format | `png` | `png`, `jpg` | `WOOGAC_CROP_FORMAT` |
| `-h`,<br/> `--height <height>` | Target height to crop image to. This value sets the height of the crop rectangle. If the value is bigger than the image height, the image height will be used instead. | - | - | - |
| `-w`,<br/> `--width <width>` | Target width to crop image to. This value sets the width of the crop rectangle. If the value is bigger than the image width, the image width will be used instead. | - | - | - |
| `-p`<br/>, `--name-pattern <name_pattern>` | A name pattern to use for the output file. Each provided image file will be renamed according to this pattern. The command uses two variables which can be used to control the final file name:<br/>* `{name}`: the original file name without file extension<br/>* `{ext}`: the new file extension based on the provided `--format` | `{name}.{ext}` | - | `WOOGAC_CROP_NAME_PATTERN` |
| `--output-format <output-format>` | The output format. The format is either plain text file. Each line contains the `file-path` `width` and `height` and the `checksum` separated by a space character. Or a json hashmap"| `plain` | `json`, `plain` | `WOOGAC_CROP_OUTPUT_FORMAT` |


## ARGS

| name         | description                         |
| ------------ | ----------------------------------- |
| `<FILES>...` | input file[s] to crop               |

## Examples

Here are a few examples to show some basic use cases

#### crop image to 40px by 80px with the default format

`woogac crop --width 40 --height 80 image.png`

#### crop multiple images to 40px by 80px with the to jpg format

`woogac crop --width 40 --height 80 --format jpg image1.png image2.png`

#### save images in different directory after resize

`woogac crop --width 20 --height 20 --output-dir export image1.png image2.png`

#### rename images with pattern

`woogac crop --width 20 --height 20 --name-patter '{name}_sm.{ext}' image1.png image2.png`

#### change report output format to json

`woogac crop --width 20 --output-format json image1.png`

#### force override of existing files

`woogac pack --force image1.png image2.png`
