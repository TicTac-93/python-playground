# --------------
# Import Modules
# --------------
import os
import sys
import pymxs
import MaxPlus

# For 3ds Max - Temporarily add this file's directory to PATH
sys.path.append(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))

import util_pymxs as util

# --------------
# Shorthand Vars
# --------------
# Max modules
rt = pymxs.runtime
maxScript = MaxPlus.Core.EvalMAXScript

# Utility functions
max_out = util.max_out
pad_string = util.pad_string
get_obj_props = util.get_obj_props
get_instances = util.get_instances

# ---------------
# Rando Functions
# ---------------
def dump_obj_info(x):
    """
    Print out all the properties of the given object
    :param x: The input object
    :return: True, unless object doesn't exist.
    """
    max_out('----- Properties -----')

    for i in get_obj_props(x):
        max_out(pad_string(str(i), str(rt.getProperty(x, i)), 25, '-'))

    max_out('----- End Properties -----')


# Stuff
max_out('Hello, Max!')

# ----------------
# Layer Operations
# ----------------
layerCount = rt.layerManager.count
hiddenLayers = []

# Iterate over Max layers, append name of hidden layers to hiddenLayers[]
for i in range(layerCount-1):
    if not rt.layerManager.getLayer(i).on:
        hiddenLayers.append(str(rt.LayerManager.getLayer(i).name))


max_out('----- Layer Info -----')
max_out('Number of Layers in current scene: ' + str(layerCount))
max_out('Number of Hidden Layers in current scene: ' + str(len(hiddenLayers)))
max_out(hiddenLayers)

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
for tgtObj in rt.lights:
    # Skip this obj if it's in the ignore list
    if tgtObj.name in lights_ignoreList:
        continue

    max_out('===== ' + str(tgtObj.name) + ' =====')

    # Print instances, if there are any
    tgt_instances = get_instances(tgtObj)
    if len(tgt_instances) > 1:
        max_out('----- ' + str(len(tgt_instances)) + ' Instances -----')

        for i in tgt_instances:
            # max_out(i.name)
            lights_ignoreList.append(i.name)

    # Check if this light has an "on" or "enabled" property.  Dump obj properties if it doesn't.
    propCheck = False
    if rt.isProperty(tgtObj, 'on'):
        max_out("Has 'On' property")
        propCheck = True
    if rt.isProperty(tgtObj, 'enabled'):
        max_out("Has 'Enabled' property")
        propCheck = True
    if not propCheck:
        dump_obj_info(tgtObj)

    max_out('')
