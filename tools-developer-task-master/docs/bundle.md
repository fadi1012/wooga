# bundle

bundle assets and resources into one bundle archive.

## Usage

`woogac bundle [FLAGS] [OPTIONS] <DIR>`

## Flags

| name              | description                                           |
| ----------------- | ----------------------------------------------------- |
| `-f`, `--force`   | overwrite existing file                               |
| `-h`, `--help`    | Prints help information                               |
| `-V`, `--version` | Prints version information                            |

## Options

| name                             | description                 | default value | possible values           | env                      |
| -------------------------------- | --------------------------- | ------------- | ------------------------- | ------------------------ |
| `--include <include-pattern>...` | file pattern to include     | `*`           | -                         | -                        |
| `--exclude <exclude-pattern>...` | file pattern to exclude     | ``            | -                         | -                        |
| `-o`, `--output-dir <Dir>`       | Output directory to use.    | -             | -                         | `PWD`                    |
| `--file-name <file_name>`        | The file name of for bundle | `bundle.zip`  | -                         | `WOOGAC_BUNDLE_FILENAME` |

## ARGS

| name         | description                     |
| ------------ | ------------------------------- |
| `<DIR>`      | directory with assets to bundle |

## Examples

Here are a few examples to show some basic use cases

#### create bundle from provided directory

`woogac bundle dir`

This will create a bundle with all files located in the provided directory. Subfolders will also be bundled. The bundle will be saved in the current working directory with the name `bundle.zip`

#### set file name for bundle

`woogac bundle --file-name custom_bundle.zip dir`

#### export bundle to a different directory

`woogac bundle --output-dir export/path dir`

This exports the bundle to the provided directory `export/path`. The directory must exist before executing.

#### set include filter for bundling

Giving the following directory structure

```plain
dir/
├── airplane_cast.png
├── airplane_cover.png
├── airplane_item.png
├── angel_cast.png
├── angel_cover.png
├── angel_item.png
├── awning_cast.png
├── awning_cover.png
├── awning_item.png
├── background.png
├── bag_cast.png
├── bag_cover.png
├── bag_item.png
```

`woogac bundle --include '*_item*' dir`

Will bundle only files matching the include glob pattern.

Multiple `--include` filter can be provided.

`woogac bundle --include '*_item*' --include 'bag_cover*' dir`

#### set exclude filter for bundling

Giving the following directory structure

```plain
dir/
├── airplane_cast.png
├── airplane_cover.png
├── airplane_item.png
├── angel_cast.png
├── angel_cover.png
├── angel_item.png
├── awning_cast.png
├── awning_cover.png
├── awning_item.png
├── background.png
├── bag_cast.png
├── bag_cover.png
├── bag_item.png
```

`woogac bundle --exclude '*_cast*' dir`

Will bundle all files except files which match the provided glob pattern.

#### set exclude/include filter for bundling for directories

The exclude and include glob filter work not only on filenames

```plain
dir/
├── 001-01
│  └── scene
│     ├── airplane_cast.png
│     ├── airplane_cover.png
│     ├── airplane_item.png
│     ├── angel_cast.png
│     ├── angel_cover.png
│     ├── angel_item.png
│     ├── awning_cast.png
│     ├── awning_cover.png
│     ├── awning_item.png
│     ├── background.png
│     ├── bag_cast.png
│     ├── bag_cover.png
│     └── bag_item.png
└── 001-02
   └── scene
      ├── angel_cast.png
      ├── angel_item.png
      ├── background.png
      ├── bag_cast.png
      ├── bag_cover.png
      ├── bag_item.png
      ├── ball_cast.png
      ├── ball_cover.png
      ├── ball_item.png
      ├── beads_cast.png
      └── beads_item.png
```

`woogac bundle --include '*001-02*' dir`

will only include files which contain `001-02` in their file-path.
