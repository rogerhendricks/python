#import untangle
import xmltodict
import xml.etree.ElementTree as ET

tree = ET.parse('bio.xml')
root = tree.getroot()


for child in root.iter('value'):
#	print (child.tag, child.attrib, child.text)
#	print(list(child.attrib()))
#	print(child.get('name'), child.text)
	child_list = {}
	values = child.text
#	print(values)
	keys = child.get('name')
#	print(keys)
	for i in keys:
		child_list[keys]= values
	print(child_list)
	


