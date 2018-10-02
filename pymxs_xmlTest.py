# --------------
# Import Modules
# --------------
import os
import sys
import pymxs
import xml.etree.ElementTree as ET

# For 3ds Max - Temporarily add this file's directory to PATH
sys.path.append(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

import util_pymxs as util

# --------------
# Shorthand Vars
# --------------
rt = pymxs.runtime

# Utility functions
max_out = util.max_out
pad_string = util.pad_string
get_obj_props = util.get_obj_props
get_instances = util.get_instances
xml_indent = util.xml_indent

# Stuff
max_out('Hello, Max!')

# Set up XML object
xmlTree = ET.ElementTree(ET.Element('root'))
xmlRoot = xmlTree.getroot()
xmlLayers = ET.SubElement(xmlRoot, 'Layers')
xmlLights = ET.SubElement(xmlRoot, 'Lights')

# ----------------
# Layer Operations
# ----------------
layerCount = rt.layerManager.count

# Add list of layers in scene to XML object
for i in range(layerCount-1):
    thisLayer = rt.layerManager.getLayer(i)
    ET.SubElement(xmlLayers, thisLayer.name.strip().replace(' ', '_'), {'trueName': thisLayer.name, 'on': str(thisLayer.on)})


max_out('----- Layer Info -----')
max_out('Number of Layers in current scene: ' + str(layerCount))
max_out('Number of Hidden Layers in current scene: ' + str(len(xmlRoot.findall("./Layers/[@on='True']"))))

# Examples of doing stuff with layers, given a list of layer names
# for l in hiddenLayers:
#    tgtLayer = rt.LayerManager.getLayerFromName(l)  # Accesses a layer using its name
#    tgtLayer.setParent(rt.LayerManager.getLayer(0))  # Sets layer parent to 0 (default)
#    tgtLayer.on = True  # Sets the layer to be 'on', aka unhidden


# ----------------
# Light Operations
# ----------------
lightCount = rt.lights.count  # Max has several baked-in selection sets, such as lights, helpers, objects, etc.
lightsOn = []
lightsOff = []

max_out('----- Light Info -----')
max_out('Number of Lights in current scene: ' + str(rt.lights.count))

lights_ignoreList = []

# Iterate over all lights, print their properties
for thisLight in rt.lights:
    # Skip this obj if it's in the ignore list
    if thisLight.name in lights_ignoreList:
        continue

    # Print instances, if there are any
    tgt_instances = get_instances(thisLight)
    if len(tgt_instances) > 1:
        for i in tgt_instances:
            # max_out(i.name)
            lights_ignoreList.append(i.name)

    # Create entry for this light in XML object
    thisLightXML = ET.SubElement(xmlLights, thisLight.name.strip().replace(' ', '_'), {'trueName': thisLight.name, 'instances': str(len(tgt_instances)-1)})
    # Check if this light has an "on" or "enabled" property - save their state to the XML object if they do
    if rt.isProperty(thisLight, 'on'):
        thisLightXML.set('on', str(thisLight.on))
    if rt.isProperty(thisLight, 'enabled'):
        thisLightXML.set('enabled', str(thisLight.enabled))

max_out('Number of Unique Lights: ' + str(rt.lights.count - len(lights_ignoreList)))

xml_indent(xmlRoot)

outputPath = os.path.dirname(__file__) + '\\radishTest.xml'
max_out('Writing ' + outputPath)
xmlTree.write(outputPath)
