import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import createNodes as cn

def main():
    cn.choiceNode(create = 'polyCylinder', name = 'model')