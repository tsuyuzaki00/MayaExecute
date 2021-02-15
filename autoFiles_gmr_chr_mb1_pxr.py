import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import autoFiles as afs

autofile = afs.AutoFile(mayaName = 'test')
dl = ['help_grp_mb', 'guide']
pl = [{'parent':'gmr_chr_mb1_pxr_grp', 'child':'mb1Rig'}]
autofile.animEXFile(deleteLists = dl, parentLists = pl)