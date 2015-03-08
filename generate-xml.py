from lxml import etree
from pathlib import Path
import cairosvg
import os
import shutil

src_path = Path('./material-design-icons/')
sprite_files = list(src_path.glob('**/svg/production/*48px.svg'))
files_element = etree.Element("files")

# set up the output dir
out = Path('gen/')
icons_out = Path(out, 'icons/')

if out.exists and out.is_dir():
	shutil.rmtree(str(out))

icons_out.mkdir(parents=True)

for f in sprite_files:
	element = etree.SubElement(files_element, 'file')
	element.text = str(f)
	element.set('id', f.stem)
	element.set('name', f.stem)

	icon_name = f.stem + '.png'
	element.set('icon', str(os.path.join(str(icons_out.relative_to(out)), icon_name)))

	with open(os.path.join(str(icons_out), icon_name),'wb+') as icon_out:
		thumb = cairosvg.svg2png(file_obj=str(f), write_to=icon_out)

stylesheet = etree.parse('stylesheet.xsl')
transform = etree.XSLT(stylesheet)

result = transform(files_element)

result.write(os.path.join(str(out), 'Definition.xml'), pretty_print=True)
