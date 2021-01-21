import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import createNodes as cn

cn.choiceNode(create = 'ambientLight', name = 'cut')