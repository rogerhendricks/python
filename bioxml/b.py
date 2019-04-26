from lxml import etree
 
#----------------------------------------------------------------------
def BioXML(xmlFile):
    """"""
 
    context = etree.iterparse(xmlFile)
    dev_dict = {}
    device = []
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print (elem.tag + " => " + text)
        dev_dict[elem.tag] = text
        if elem.tag == "value":
            device.append(dev_dict)
            dev_dict = {}
    return device
 
if __name__ == "__main__":
    BioXML("bio.xml")
