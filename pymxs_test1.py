# Import PyMXS, MaxPlus, and set up shorthand vars
import pymxs
import MaxPlus
import util_pymxs

# PyMXS variable setup
rt = pymxs.runtime

# MaxPlus variable setup
maxScript = MaxPlus.Core.EvalMAXScript

# Utility Functions
u = util_pymxs


# Stuff
u.max_out('Hello, Max!')

# ----------------
# Layer Operations
# ----------------
layerCount = rt.layerManager.count
hiddenLayers = []

# Iterate over Max layers, append name of hidden layers to hiddenLayers[]
for i in range(layerCount-1):
    if not rt.layerManager.getLayer(i).on:
        hiddenLayers.append(str(rt.LayerManager.getLayer(i).name))


u.max_out('----- Layer Info -----')
u.max_out('Number of Layers in current scene: ' + str(layerCount))
u.max_out('Number of Hidden Layers in current scene: ' + str(len(hiddenLayers)))
u.max_out(hiddenLayers)

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

u.max_out('----- Light Info -----')
u.max_out('Number of Lights in current scene: ' + str(rt.lights.count))

# Iterate over all lights, print their baseObject, name
# for i in rt.lights:
#    u.max_out(str(i.baseObject) + ' -- ' + str(i.name))

# Print all properties of first light
u.max_out('----- Properties of ' + str(rt.lights[0].name) + ' -----')

lightProps = u.get_obj_props(rt.lights[0])

for i in lightProps:
    u.max_out(u.pad_string(str(i), str(rt.getProperty(rt.lights[0], i)), 25, '-'))

u.max_out('----- End Properties -----')
