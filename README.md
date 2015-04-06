# Material Icons for Pencil
All 700+ of Google's [Material Design Icons](https://github.com/google/material-design-icons) as a [Pencil](https://github.com/prikhi/pencil) stencil collection.

Based on the 48px version of the icons, however everything is in vector format, so can be scaled to any size.

## Installation
- Download the [latest release](https://github.com/nathanielw/Material-Icons-for-Pencil/releases/latest) zip file.
- Install the collection in Pencil by going to *Tools > Install new collection* and selecting the zip.
- Enjoy!

## Generating the Collection
- Clone this repo with the `--recursive` flag to include submodules. (or just clone it normally then `git submodule init` and `git submodule update`)
- Run the `generate-xml.py` script (tested with Python 3.4).

This will generate the stencil definition XML and png thumbnails and place them in the `gen/` folder.

Everything **inside** the `gen/` folder can then be zip'd and installed in Pencil.

## License
[Material Design Icons](https://github.com/google/material-design-icons) by Google are released under an [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license.

All source code/scripts used to generate the Pencil stencil are released under the [MIT License](http://opensource.org/licenses/mit-license.php).
