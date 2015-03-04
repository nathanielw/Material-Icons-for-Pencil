from lxml import etree
from pathlib import Path

path = Path('./material-design-icons-master/sprites/svg-sprite/')
print(list(path.glob('**/*.svg')))

root = etree.Element("files")

# Loop over files, add to xml
