import sys
import os
from maya import cmds

sys.path.append(os.path.abspath(".."))
from MayaLibrary import mayaJsons as mjs

def main():
    filePath = cmds.file(q=True, sn=True)
    sceneName = os.path.splitext(os.path.basename(filePath))[0] 
    mayaName = sceneName.replace('proxyWork', 'pxr')
    jsonName = os.path.splitext(os.path.basename(__file__))[0]
    mayaJsonMake = mjs.MayaJsonMake(mayaName = mayaName, jsonName = jsonName) 
    sels = cmds.ls(sl = True)
    mayaJsonMake.selTwoParentLists(parent = sels[0], child = sels[1])