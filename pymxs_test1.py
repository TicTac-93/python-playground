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

# Iterate over all lights, print their baseObject, name
# for i in rt.lights:
#    max_out(str(i.baseObject) + ' -- ' + str(i.name))

# Print all properties of first light
max_out('----- Properties of ' + str(rt.lights[0].name) + ' -----')

lightProps = get_obj_props(rt.lights[0])

for i in lightProps:
    max_out(pad_string(str(i), str(rt.getProperty(rt.lights[0], i)), 25, '-'))

max_out('----- End Properties -----')
