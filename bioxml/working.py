import untangle
import xmltodict

with open('bio.xml') as fd:
	doc = xmltodict.parse(fd.read())

doc['mydocument']['plus']['#text']

print(doc['mydocument']['plus']['#text'])



