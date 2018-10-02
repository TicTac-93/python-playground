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


# Use element.text and element.tail to apply indents and newlines
def xml_indent(el, depth=0, careful=False):
    """
    Formats an XML ETree with newlines and indents.
    By default, assumes that nothing is stored in el.text or el.tail.
    :param el: Root element of XML tree.
    :param depth: Used for recursive calls, stores depth in tree.
    :param careful: Checks for content in el.text and el.tail before overwriting.
    :return: None - Operates on existing tree.
    """
    # Prep newline and indent for child elements
    i = "\n" + depth*"\t"

    # Check if we're being careful or not, switch accordingly
    # If careful, append indent to contents of el.text and el.tail

    # If careless, replace contents
    if not careful:
        if len(el):
            el.text = i + "\t"  # Newline + Indent sub-elements
            el.tail = i  # Add newline after closing tag
            for el in el:  # Use same variable so that the last element in loop will remain accessible
                xml_indent(el, depth + 1)
            el.tail = i  # De-indent closing tag
        else:  # If there aren't sub-elements, just add a newline
            if not el.tail or not el.tail.strip():
                el.tail = i


# Create a new tree
myTree = ET.ElementTree(ET.Element('root'))
# Get the root (aka, only node in the tree)
myRoot = myTree.getroot()
# Create sub-elements, using the ElementTree method
subEl1 = ET.SubElement(myRoot, 'subEl-1', {'attrib1': 'A', 'attrib2': 'B', 'attrib3': 'C'})
subEl2 = ET.SubElement(myRoot, 'subEl-2', {'attrib1': 'D', 'attrib2': 'E', 'attrib3': 'F'})
ET.SubElement(subEl1, 'subEl-1a', {'foo': 'bar', 'blah': 'blub'})

xml_indent(myRoot)
myTree.write('myXML.xml')
