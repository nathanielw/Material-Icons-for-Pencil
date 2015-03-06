from lxml import etree
from pathlib import Path
import cairosvg
import os
import shutil

src_path = Path('./material-design-icons/')
sprite_files = list(src_path.glob('**/svg/production/*48px.svg'))
file_element = etree.Element("files")

# set up the output dir
out = Path('gen/')
icons_out = Path(out, 'icons/')

if out.exists and out.is_dir():
	shutil.rmtree(str(out))

icons_out.mkdir(parents=True)

for f in sprite_files:
	element = etree.SubElement(file_element, "file")
	element.text = str(f)

	with open(os.path.join(str(icons_out), f.stem + '.png'),'wb+') as out:
		thumb = cairosvg.svg2png(file_obj=str(f), write_to=out)


print(etree.tostring(file_element))
