##########################################################################
#Author: Nataly
#Date: 08.12.2021
#Task: Create XML tree with root <shop> and different products from 
# category "Vegan products". Write XML tree to file.
# Create XmlTreeHelper class to add tags into tree.
# Products should contain information about:
# - product name
# - type
# - producer
# - price
# - currency
##########################################################################

# import XmlTreeHelper class from Packages
import Packages.XmlTreeHelper as HP

# import package to work with xml format
import xml.etree.ElementTree as ET

# create root element of of XML tree
root = ET.Element('shop')

# create child element with name of products category
category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

# define some products in added category
product_1 = ET.SubElement(category, 'product', {'name': 'Good Morging Sunshine'})
product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})

# create object of class XmlTreeHelper
xml_tree_helper = HP.XmlTreeHelper()

# fill tags with product data
xml_tree_helper.add_tags_with_text(product_1, {
    'type': 'cereals',
    'producer': 'Food Limited',
    'price': '9.90',
    'currency': 'USD'
    })

xml_tree_helper.add_tags_with_text(product_2, {
    'type': 'pasta',
    'producer': 'Programmers Eat Pasta Gmbh',
    'price': '14.49',
    'currency': 'EUR'
    })

xml_tree_helper.add_tags_with_text(product_3, {
    'type': 'beverages',
    'producer': 'Food Drinks4Coders Inc.',
    'price': '19.75',
    'currency': 'USD'
})

# create tree and write it into file
tree = ET.ElementTree(root)
tree.write('shop.xml', 'UTF-8', True)