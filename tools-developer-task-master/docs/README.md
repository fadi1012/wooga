# woogac

`woogac` is a multi purpose utility tool. It is designed as a blackbox utility tool that
can execute a manyfold of different tasks. It's main purpose for this task is to simulate one or
many closed source third party command-line tools.

## Usage

`woogac [FLAGS] [OPTIONS] [SUBCOMMAND]`

## Flags

| name             | description                                           |
| ---------------- | ----------------------------------------------------- |
| `-h`, `--help`   | Prints help information                               |
| `-V`, `--version`| Prints version information                            |
| `-v`, `--verbose`| output verbosity                                      |

## Options

| name              | description     | default value | possible values           | env              |
| ----------------- | --------------- | ------------- | ------------------------- | ---------------- |
| `--color <color>` | Output coloring | `auto`        | `auto`, `always`, `never` | `WOOGAC_COLOR`   |
| `--log-dir <log>` | path to log dir | -             | -                         | `WOOGAC_LOG_DIR` |

## Subcommands

| name         | description                                                 |
| ------------ | ----------------------------------------------------------- |
| [bundle]     | bundle assets and resources into one bundle archive         |
| [checksum]   | calculates `sha256` checksums for provided file[s]          |
| [crop]       | Crop image from center with provided width and height       |
| help         | Prints this message or the help of the given subcommand(s)  |
| [image-info] | reads image informations for provided file[s]               |
| [pack]       | Pack images into one big texture Atlas                      |
| [resize]     | Resize a set of image files.                                |

[bundle]:     bundle.md
[checksum]:   checksum.md
[crop]:       crop.md
[image-info]: image-info.md
[pack]:       pack.md
[resize]:     bundle.md
