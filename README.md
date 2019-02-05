# Anime torrent sorter

Searches source directory for video downloads and sorts them into directories based on the series name.

## Installation

1. Clone or download the repository
2. Navigate to the repository in terminal
3. Run `pip3 install .`

By default pip3 installs it into `~/.local/bin/`, if you don't like that talk to pip.

### Upgrade

1. Navigate to the repository in terminal
2. Run `git pull`
3. Run `pip3 uninstall --yes sort-torrents`
4. Run `pip3 install .`

### Remove

1. Navigate to the repository in terminal
3. Run `pip3 uninstall --yes sort-torrents`
4. Remove repository files


## Usage

`usage: sort-torrents [-h] --source path --dest path`

### Arguments

| **Argument**                                          | **Description**                                       | **Type**  |
| ---                                                   | ---                                                   | ---       |
| **-h, --help**                                        | Show help message and exist                           | Optional  |
| **--source [path], -s [path]**                        | Source directory to scan for matching files.          | Required  |
| **--dest [path], --destination [path], -d [path]**    | Destination directory to sort into. (default: None)   | Required  |

### Pattern

File matching regex pattern: `\[[\w\W]+\] ([\w\W]+) - ([\d]+) \[[\w\W]+\].([\w]+)`

So in other words it looks for: 

|                       | Series name        |              | Episode       |                       |           | Extension         |
| :---:                 | :---:              | :---:        | :---:         | :---:                 | :---:     | :---:             |
| `[Any charaters]`     | `Any characters`   | ` - `        | `Numers`      | `[Any caharters]`     | ` . `     | `Any characters`  |

Pattern to match files is defined inside `torrent_sorter/sorter.py` as `PATTERN`

It's created to primerly match HorribleSubs anime distributions but should catch most others.

If you wish to edit regex pattern the only requirement is to produce 3 groups in given order: name, episode, extension.


### Alias

Do yourself a favor and make an alias in `~/.zshrc` or `~/.bash_aliases` like

`alias sort-animu="sort-torrents -s /my/path/to/animu -d /my/path/to/videos"`
