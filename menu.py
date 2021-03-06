from maya import cmds

#modelingLists = {'label': '', 'icon': '.png', 'command':''}

def main():
    cmds.menu(l = 'Custom Tools', p ='MayaWindow', to = True)

    cmds.menuItem( subMenu=True, label='Setting', to = True)
    cmds.menuItem( label='LeyerSetting', c = 'from mainEdit import layerSetting as ps; reload(ps); ps.main()')
    cmds.menuItem( optionBox=True, c = 'from mainEdit import layerSetting as ps; reload(ps); ps.option()')
    cmds.menuItem( label='AutoRename', c = 'from mainEdit import autoRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='ENGIRename', c = 'from ENGI import autoRename_engi as ps; reload(ps); ps.main()')
    #cmds.menuItem( optionBox=True )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( divider = True, dividerLabel = 'Check')
    cmds.menuItem( subMenu=True, label='ExternalScript', to = True)
    cmds.menuItem( label='ModelChecker', c = 'from externalScript.modelChecker.src import modelChecker as ps; reload(ps); ps.main()')
    cmds.menuItem( label='ErrorCheckingTool', c = 'from externalScript.errorCheckingTool import ErrorCheckingTool as ps; reload(ps); ps.StartUI()')
    cmds.menuItem( label='SkinningTool', c = 'from externalScript.skinningTool import SkinningToolsUI as ps; reload(ps); ps.startUI()' )
    cmds.setParent( '..', menu=True )
    cmds.menuItem( subMenu=True, label='Inquiry', to = True)
    cmds.menuItem( label='LookNodeType', c = 'from inquiry import lookNodeType as ps; reload(ps); ps.main()')
    cmds.menuItem( label='LookSelectList', c = 'from inquiry import lookSelectList as ps; reload(ps); ps.main()')
    cmds.menuItem( label='LookSelectKeyAttr', c = 'from inquiry import lookSelectKeyAttr as ps; reload(ps); ps.main()')
    cmds.menuItem( label='LookBindJoints', c = 'from inquiry import lookBindJoints as ps; reload(ps); ps.main()')
    cmds.menuItem( label='LookShapeColor', c = 'from inquiry import lookShapeColor as ps; reload(ps); ps.main()')
    cmds.menuItem( label='LookMatrix', c = 'from inquiry import lookMatrix as ps; reload(ps); ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( divider = True, dividerLabel = 'Modeling')
    cmds.menuItem( subMenu=True, label='CreateObjects', to = True)
    cmds.menuItem( label='Cube', i = 'polyCube.png', c = 'from MayaExecute import createNodes_polyCube as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Ball',  i = 'polySphere.png', c = 'from MayaExecute import createNodes_polyBall as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Cylinder', i = 'polyCylinder.png', c = 'from MayaExecute import createNodes_polyCylinder as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Plean', i = 'polyMesh.png', c = 'from MayaExecute import createNodes_polyPlane as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='ImagePlean', i = 'ImagePlane.png', c = 'from MayaExecute import createNodes_imagePlane as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Camera', i = 'view.png', c = 'from MayaExecute import createNodes_camera as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='AmbientLight', i = 'ambientlight.png', c = 'from MayaExecute import createNodes_ambientLight as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='DirectionalLight', i = 'directionallight.png', c = 'from MayaExecute import createNodes_directionalLight as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='PointLight', i = 'pointlight.png', c = 'from MayaExecute import createNodes_pointLight as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='SpotLight',  i = 'spotlight.png', c = 'from MayaExecute import createNodes_spotLight as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Locator', i = 'locator.png', c = 'from mainEdit import spaceLocatorCreateRename as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Joint', i = 'kinJoint.png', c = 'from mainEdit import jointCreateRename as ps; reload(ps); ps.main()' )
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( subMenu=True, label='ModelingEdit', to = True)
    cmds.menuItem( label='GeometryReset', c = 'from modelEdit import freezeResetHisDel as ps; reload(ps); ps.main()')
    cmds.menuItem( label='CornerEdge', i = 'cornerEdge.png', c = 'from modelEdit import cornerEdgeSelect as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Combine', i = 'polyUnite.png', c = 'from modelEdit import combineMesh as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Extract' , i = 'polyChipOff.png', c = 'from modelEdit import extractComponent as ps; reload(ps); ps.main()')
    cmds.menuItem( label='HardEdge', i = 'polyHardEdge.png', c = 'from modelEdit import hardEdge as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='SoftEdge', i = 'polySoftEdge.png', c = 'from modelEdit import softEdge as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='CamImageOffConnect', c = 'from modelEdit import camImageOffsetConnection as ps; reload(ps); ps.main()' )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( divider = True, dividerLabel = 'Rigging')
    cmds.menuItem( subMenu=True, label='Skin', to = True)
    cmds.menuItem( label='SkinPaintValue', i = 'skinPaintValue.png', c = 'from mainEdit import skinPaintValue as ps; reload(ps); ps.main()' )
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( subMenu=True, label='CreateCurves', to = True)
    cmds.menuItem( label='Antenna', c = 'from MayaExecute import setCurves_antenna as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Arrow1', c = 'from MayaExecute import setCurves_arrow1 as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Arrow2', c = 'from MayaExecute import setCurves_arrow2 as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Arrow4', c = 'from MayaExecute import setCurves_arrow4 as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Circle', c = 'from MayaExecute import setCurves_circle as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Cube', c = 'from MayaExecute import setCurves_cube as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Hexagon', c = 'from MayaExecute import setCurves_hexagon as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Pyramid', c = 'from MayaExecute import setCurves_pyramid as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Square', c = 'from MayaExecute import setCurves_square as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Twist', c = 'from MayaExecute import setCurves_twist as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='VectorIK', c = 'from MayaExecute import setCurves_vectorIK as ps; reload(ps); ps.main()' )
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='Constraint', to = True )
    cmds.menuItem( label='IkHandle', i = 'kinHandle.png', c = 'from createRenames import ikHandleCreateRename as ps; reload(ps); ps.main()' )
    cmds.menuItem( label='Parent', i = 'parentConstraint.png', c = 'from constraints import parentConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Point', i = 'posConstraint.png', c = 'from constraints import pointConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Orient', i = 'orientConstraint.png', c = 'from constraints import orientConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Scale', i = 'scaleConstraint.png', c = 'from constraints import scaleConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='Aim', i = 'aimConstraint.png', c = 'from constraints import aimConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='PoleVector', i = 'poleVectorConstraint.png', c = 'from constraints import poleVectorConstraintRename as ps; reload(ps); ps.main()')
    cmds.menuItem( label='JointMatrix', c = 'from constraints import matrixJointConnect as ps; reload(ps); ps.main()')
    cmds.menuItem( label='ParentMatrix', c = 'from constraints import matrixParentConnect as ps; reload(ps); ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='MirrorEdit', to = True )
    cmds.menuItem( label='CurveEditMirror', c = 'from mainEdit import curveMirror as ps; reload(ps); ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='SelectsEdit', to = True )
    cmds.menuItem( label='CtrlColorChange', c = 'from selectsEdit import ctrlColorChenge as ps; reload(ps); ps.main()')
    cmds.menuItem( label='CtrlColorFreeChange', c = 'from selectsEdit import ctrlColorFreeChenge as ps; reload(ps); ps.main()')
    cmds.menuItem( divider = True, dividerLabel = '')
    cmds.menuItem( label='CurveInSelects', c = 'from selectsEdit import curveInSelect as ps; reload(ps); ps.main()')
    cmds.menuItem( label='JointRadiusEdit', c = 'from selectsEdit import jointRadius as ps; reload(ps); ps.main()')
    cmds.menuItem( optionBox=True, c = 'from selectsEdit import jointRadius as ps; reload(ps); ps.option()')
    cmds.setParent( '..', menu=True )
    
    cmds.menuItem( divider = True, dividerLabel = 'Animator')
    cmds.menuItem( subMenu=True, label='CreateCtrl', to = True )
    cmds.menuItem( label='AddNullNode', c = 'from mainEdit import addNullNode as ps; reload(ps); ps.main()')
    cmds.menuItem( label='OffsetCtrl', c = 'from mainEdit import ctrlOneConnect as ps; reload(ps); ps.main()')
    cmds.setParent( '..', menu=True )

    cmds.menuItem( subMenu=True, label='Keyframe', to = True)
    #cmds.menuItem( label='GrpCtrlAllKey', c = 'from mainEdit import grpCtrlAllKey as ps; ps.main()')
    cmds.setParent( '..', menu=True )
