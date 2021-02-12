import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import setCurves as sc

def main():
    sels = pm.selected()
    setCurve = sc.SetCurve(name = 'curve')
    if sels == []:
        curve = setCurve.curveHexagon()
    else :
        for sel in sels:
            curve = setCurve.curveHexagon()
            trs = setCurve.trsSetting(ctrl = curve)
            setCurve.selectPosition(sel = sel, trs = trs)
        
