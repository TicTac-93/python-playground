# Practice and experimentation with the ETree library
import xml.etree.ElementTree as ET

# Load the test.xml file from this directory
tree = ET.parse('test.xml')
root = tree.getroot()


# Print the root element, and its immediate children.
# Can iterate over child nodes.
print root.tag, root.attrib
for el in root:
    print "  ", el.tag, el.attrib

print"""
==========
"""

# Prints the whole tree
# the iter method will iterate over the entire tree, and can filter by element name.
for el in root.iter():  # Iterate over whole tree
    print el.tag, el.attrib, el.text

print"""
==========
"""

# Print only country and rank
for country in root.iter('country'):
    name = country.get('name')  # Get the 'name' attribute of the country element
    rank = country.find('rank').text  # Find the first child element named 'rank', and get its text value
    print name, rank

print"""
=======================
Working with Custom XML
=======================
"""

# Create a new tree
myTree = ET.ElementTree(ET.Element('root'))
# Get the root (aka, only node in the tree)
myRoot = myTree.getroot()
# Create a sub-element, using the ElementTree method
ET.SubElement(myRoot, 'subEl-1', {'attrib1': 'A', 'attrib2': 'B', 'attrib3': 'C'})
ET.SubElement(myRoot, 'subEl-2', {'attrib1': 'D', 'attrib2': 'E', 'attrib3': 'F'})
for el in myRoot.iter():
    print el.tag, el.attrib
