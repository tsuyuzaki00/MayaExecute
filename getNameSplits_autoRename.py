import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import getNameSplits as gns

def main():
    sels = pm.selected()
    getNameSplit = gns.GetNameSplit()
    for sel in sels:
        scene = getNameSplit.scene()
        node = getNameSplit.node(sel)
        obj = getNameSplit.obj(sel)
        pos = getNameSplit.pos(sel)
        num = getNameSplit.num(sel)
        lists = [pos,obj,node,scene,num]
        names = [l for l in lists if l != '']
        autoRename = '_'.join(names)
        if sel != autoRename:
            trueRename = getNameSplit.sameNameCheck(check = autoRename)
            pm.rename(sel, trueRename)