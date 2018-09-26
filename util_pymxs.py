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


def get_instances(x):
    """
    A short MaxScript snippet to get instances of an object and return their objects in an array.
    :param x: The input object
    :return: An array of Max objects.  If there are no instances, it will only contain the source object.
    """
    instanceNames = maxScript('InstanceMgr.GetInstances $' + x.name + """ &instances
    out = #()
    for i in instances do append out i.name
    out""").Get()

    instanceObjs = []
    for i in instanceNames:
        instanceObjs.append(rt.getNodeByName(i))

    return instanceObjs
