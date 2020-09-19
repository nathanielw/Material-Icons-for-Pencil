from lxml import etree
from pathlib import Path
import cairosvg
import os
import shutil
import re

sprite_files = sorted(list(Path('./MaterialDesign/icons/svg/').glob('*.svg')), key=lambda file: file.as_posix())
files_element = etree.Element("files")

# set up the output dir
out = Path('gen/')
icons_out = Path(out, 'icons/')
svgs_out = Path(out, 'vectors/')

if out.exists and out.is_dir():
	shutil.rmtree(str(out))

icons_out.mkdir(parents=True)
svgs_out.mkdir(parents=True)

for f in sprite_files:
	element = etree.SubElement(files_element, 'file')
	element.text = f.as_posix()
	element.set('id', f.stem)

	element.set('name', (f.stem.replace('-', ' ')).title())

	icon_name = f.stem + '.png'
	element.set('icon', icons_out.relative_to(out).joinpath(icon_name).as_posix()) # Pencil uses Unix-style paths for icons

	svg_file = open(str(f), 'rb')
	svg_dest_file = open(os.path.join(str(svgs_out), f.stem + '.svg'), 'wb+')
	shutil.copyfileobj(svg_file, svg_dest_file)

	with open(os.path.join(str(icons_out), icon_name),'wb+') as icon_out:
		thumb = cairosvg.svg2png(file_obj=svg_file, write_to=icon_out)



stylesheet = etree.parse('stylesheet.xsl')
transform = etree.XSLT(stylesheet)

result = transform(files_element)

result.write(os.path.join(str(out), 'Definition.xml'), pretty_print=True)
