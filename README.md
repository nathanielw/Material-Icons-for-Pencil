# Material Icons for Pencil
All 800+ of Google's [Material Design Icons](https://github.com/google/material-design-icons) as a [Pencil](https://github.com/prikhi/pencil) stencil collection.

Based on the 24px version of the icons, however everything is in vector format, so can be scaled to any size.

*Check out my other stencil collections for Pencil at [nathanielw.github.io/pencil-stencils](http://nathanielw.github.io/pencil-stencils/)*

## Installation
- Download the [latest release](https://github.com/nathanielw/Material-Icons-for-Pencil/releases/latest) zip file.
- Install the collection in Pencil by going to *Tools > Install new collection* and selecting the zip.
- Enjoy!

### Updating
Right-click on the collection in Pencil's sidebar and choose _Uninstall this collection_ before repeating the installation steps.

## Generating the Collection
- Clone this repo with the `--recursive` flag to include submodules. (or just clone it normally then `git submodule init` and `git submodule update`)
- Run the `generate-xml.py` script (tested with Python 3.4).

This will generate the stencil definition XML and png thumbnails and place them in the `gen/` folder.

Everything **inside** the `gen/` folder can then be zip'd and installed in Pencil.

Windows users wanting to **generate** the collection: see [this comment](https://github.com/nathanielw/Material-Icons-for-Pencil/issues/2#issuecomment-108849198).

## License
[Material Design Icons](https://github.com/google/material-design-icons) by Google are released under an [Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) license.

All source code/scripts used to generate the Pencil stencil are released under the [MIT License](http://opensource.org/licenses/mit-license.php).
