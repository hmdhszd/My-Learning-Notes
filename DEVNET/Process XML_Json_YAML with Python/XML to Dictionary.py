import xmltodict
from pprint import pprint

xml_example = open("example_XML_file.xml").read()
pprint(xml_example)

print("\n\n\n\n")


xml_dict = xmltodict.parse(xml_example)
pprint(xml_dict)

