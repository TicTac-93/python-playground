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
