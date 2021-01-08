import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import mayaRender as mr

def main():
    mr.runPlayblast(cam = 'C_joe_bodySkinCheck_00_cam', fileName = 'joe_bodySkinCheck', workSpacePath="D:/GMR/cjoe", startFrame = 0, endFrame = 1200)

main()