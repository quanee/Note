
# re

import re

text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found:
    print(title)


# DOM

from xml.dom.minidom import parse, Node

xmltree = parse('mybooks.xml')