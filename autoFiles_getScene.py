import sys
import os
from maya import cmds
sys.path.append(os.path.abspath(".."))
from MayaLibrary import autoFiles as afs

import json

def main():
    filePath = cmds.file(q=True, sn=True)
    sceneName = os.path.splitext(os.path.basename(filePath))[0] 
    mayaName = sceneName.replace('Work', '')
    autofile = afs.AutoFile(mayaName = mayaName)
    with open(autofile.filePass(), 'r') as f:
        roots = json.load(f)
        dl = roots[0]
        pl = roots[1]
        autofile.animEXFile(deleteLists = dl, parentList = pl)