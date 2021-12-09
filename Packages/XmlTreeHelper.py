# import package to work with xml format
import xml.etree.ElementTree as ET

class XmlTreeHelper:
    # transform tags into list of tags with text
    def add_tags_with_text(self, parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements