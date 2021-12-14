import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTreeWidgetItem
from loguru import logger
import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from util.constant import *

vtk.vtkOutputWindow.SetGlobalWarningDisplay(0)


def MakeAxesActor():
    axes = vtk.vtkAxesActor()
    axes.SetShaftTypeToCylinder()
    axes.SetXAxisLabelText('X')
    axes.SetYAxisLabelText('Y')
    axes.SetZAxisLabelText('Z')
    axes.SetTotalLength(2.0, 2.0, 2.0)
    axes.SetCylinderRadius(0.5 * axes.GetCylinderRadius())
    axes.SetConeRadius(1.025 * axes.GetConeRadius())
    axes.SetSphereRadius(1.5 * axes.GetSphereRadius())
    return axes


def flow_view(self, args):

    for i in range(self.mains["panel"].ui().tabWidget.count()):
        tabtext = self.mains["panel"].ui().tabWidget.tabText(i)
        if tabtext == '流场可视化':
            self.mains['panel'].ui().tabWidget.setCurrentIndex(i)
            return


    self.vtkWidget = QVTKRenderWindowInteractor(self.form)
    r = vtk.vtkFLUENTReader()
    r.SetFileName(os.path.join('projects', 'out.cas'))
    r.EnableAllCellArrays()
    r.Update()
    g = vtk.vtkGeometryFilter()
    g.SetInputConnection(r.GetOutputPort())

    ##########################################################
    # 显示网格

    lut = vtk.vtkLookupTable()
    lut.SetHueRange(0.667, 0)
    lut.Build()
    NAME = 'X_VELOCITY'
    scalars = r.GetOutput().GetBlock(0).GetCellData().GetArray(NAME)
    # 创建一个Cutter的Filter
    # MeshMapper = vtk.vtkCompositePolyDataMapper2()
    TempMapper = vtk.vtkCompositePolyDataMapper()
    TempMapper.SetInputConnection(g.GetOutputPort())
    TempMapper.SetScalarModeToUseCellFieldData()
    TempMapper.SelectColorArray(NAME)
    TempMapper.SetScalarRange(scalars.GetRange())
    TempMapper.SetLookupTable(lut)
    TempActor = vtk.vtkActor()
    TempActor.SetMapper(TempMapper)
    TempRen = vtk.vtkRenderer()
    TempRen.SetViewport(0.0, 0.0, 1, 1)
    TempRen.GradientBackgroundOn()
    TempRen.SetBackground(1, 1, 1)
    TempRen.SetBackground2(0.4, 0.55, 0.75)
    TempRen.AddActor(TempActor)

    ##########################################################
    self.vtkWidget.GetRenderWindow().AddRenderer(TempRen)

    iren = self.vtkWidget.GetRenderWindow().GetInteractor()
    iren.Initialize()

    iren.axes = MakeAxesActor()
    om = vtk.vtkOrientationMarkerWidget()
    om.SetOrientationMarker(iren.axes)
    om.SetInteractor(iren)
    om.EnabledOn()
    om.InteractiveOn()
    iren.om = om

    self.mains["panel"].ui().tabWidget.addTab(self.vtkWidget, QIcon(QPixmap(':/db/聚类分布138.svg')), '流场可视化')
    currentindex = self.mains["panel"].ui().tabWidget.count() - 1
    self.mains['panel'].ui().tabWidget.setCurrentIndex(currentindex)
