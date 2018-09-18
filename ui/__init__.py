import os

def getUiPath():
    return os.path.dirname(os.path.realpath(__file__))

def getBasicColors():
    baseClr = "#2166a8"
    contrastClr = "#444243"
    baseText = "#DDD"
    return [baseClr, contrastClr, baseText]
