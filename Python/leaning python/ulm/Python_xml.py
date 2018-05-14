
# re

import re

text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found:
    print(title)


# DOM

from xml.dom.minidom import parse, Node

xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)


# SAX

import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False

    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True

    def characters(self, data):
        if self.inTitle:
            print(data)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False


import xml.sax

parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)