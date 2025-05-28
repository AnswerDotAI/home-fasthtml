#!/usr/bin/env python

from fastcore.utils import *
import fastcore.xtras
from lxml import etree
from datetime import datetime, timezone

my_path = Path(__file__).parent.parent.absolute()
git_path = my_path.parent.absolute()
assert git_path.exists()
fhome_path = git_path/'home-fasthtml'
about_path = fhome_path/'about'
docs_path = fhome_path/'docs'
tools_path = fhome_path/'tools'

pages = (tools_path/'pages').read_text().strip().splitlines()
sitemap = (docs_path/'sitemap.xml').read_text()

parser = etree.XMLParser(remove_blank_text=True)
root = etree.fromstring(sitemap.encode('utf-8'), parser)

ns = root.nsmap[None]
current_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
for page in pages:
    url = etree.SubElement(root, f"{{{ns}}}url")
    loc = etree.SubElement(url, f"{{{ns}}}loc")
    loc.text = f"https://www.fastht.ml{page}"
    lastmod = etree.SubElement(url, f"{{{ns}}}lastmod")
    lastmod.text = current_time

res = etree.tostring(root, xml_declaration=True, encoding='UTF-8', pretty_print=True).decode('utf-8')
(my_path/'sitemap.xml').write_text(res)

