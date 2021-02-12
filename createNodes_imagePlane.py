import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import createNodes as cn

def main():
    node = cn.CreateNode(name = 'model')
    node.imagePlaneNode()