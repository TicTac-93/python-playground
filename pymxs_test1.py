# Import PyMXS, MaxPlus, and set up shorthand vars
import pymxs
import MaxPlus

# PyMXS variable setup
rt = pymxs.runtime

# MaxPlus variable setup
maxScript = MaxPlus.Core.EvalMAXScript


# Utility Functions
def max_out(x):
    """
    Print x to MAXScript Listener.
    """

    output = 'print "' + str(x) + '"'  # Always convert to string, to be safe
    maxScript(output)


def get_obj_props(obj):
    """
    Does what showProperties should do, and builds a dictionary of property:value pairs
    for a valid Max object.
    :param obj: The max object.
    :return: A dictionary of property:value pairs.
    """
    propList = rt.getPropNames(obj)
    propDict = {}

    for i in propList:
        propDict[i] = str(rt.getProperty(obj, i))

    return propDict


def pad_string(str1, str2, padding, x):
    """
    Concatenates two strings, padding the joint with whitespace so the second string
    begins at a certain position.  Pads with one space if it's already past that pos.
    :param str1: The first string
    :param str2: The second string
    :param padding: The minimum position for str2 to begin
    :param x: The character to pad with.  Defaults to ' '
    :return:
    """
    if x is None:
        x = ' '

    output = str1
    padding = padding - len(str1)

    if padding > 0:
        output = output + (x * padding)
    else:
        output = output + x

    output = output + str2
    return output


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
