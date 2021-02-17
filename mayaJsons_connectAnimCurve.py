import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import mayaJsons as mjs

def main():
    jsonName = "mayaJsons_connectAnimCurve"
    mayaJsonMake = mjs.MayaJsonMake(jsonName = jsonName)
    getJson = mayaJsonMake.loadJsonFolder()
    keys = 31
    for key in range(keys):
        for json in getJson:
            pm.currentTime(key)
            pm.setAttr(json["destination"] + '.' + json["attr"], pm.getAttr(json["source"] + "." + json["attr"]))
            pm.setKeyframe(json["destination"], at=json["attr"])
            
main()