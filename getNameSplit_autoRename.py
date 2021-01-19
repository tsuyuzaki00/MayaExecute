import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import getNameSplit as gns

def main():
    sels = pm.selected()
    for sel in sels:
        scene = gns.scene()
        node = gns.node(sel)
        obj = gns.obj(sel)
        pos = gns.pos(sel)
        num = gns.num(sel)
        lists = [pos,obj,node,scene,num]
        names = [l for l in lists if l != '']
        autoRename = '_'.join(names)
        pm.rename(sel, autoRename)