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


# Stuff
max_out('Hello, Max!')

layerCount = rt.layerManager.count
hiddenLayers = []
# Iterate over Max layers, append name of hidden layers to hiddenLayers[]
for i in range(layerCount-1):
    if not rt.layerManager.getLayer(i).on:
        hiddenLayers.append(str(rt.LayerManager.getLayer(i).name))


max_out('Number of Layers in current scene: ' + str(layerCount))
max_out('Number of Hidden Layers in current scene: ' + str(len(hiddenLayers)))
max_out(hiddenLayers)
