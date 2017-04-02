import markdown
import codecs

input_file = codecs.open('UNIXmd.md', mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)