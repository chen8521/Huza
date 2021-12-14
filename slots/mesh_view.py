import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QHBoxLayout, QWidget, QToolBar, QAction
from loguru import logger
import vtkmodules.all as vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from util.constant import *

vtk.vtkOutputWindow.SetGlobalWarningDisplay(0)


def ViewDirection(renderer, lookX, lookY, lookZ, upX, upY, upZ):
    renderer.GetActiveCamera().SetPosition(0, 0, 0)  # 相机位置
    renderer.GetActiveCamera().SetFocalPoint(lookX, lookY, lookZ)  # 焦点位置
    renderer.GetActiveCamera().SetViewUp(upX, upY, upZ)  # 朝上方向
    renderer.ResetCamera()
    renderer.GetRenderWindow().Render()


def ViewPositiveX(renderer):
    ViewDirection(renderer, 1, 0, 0, 0, 0, 1)


def ViewNegativeX(renderer):
    ViewDirection(renderer, -1, 0, 0, 0, 0, 1)


def ViewPositiveY(renderer):
    ViewDirection(renderer, 0, 1, 0, 0, 0, 1)


def ViewNegativeY(renderer):
    ViewDirection(renderer, 0, -1, 0, 0, 0, 1)


def ViewPositiveZ(renderer):
    ViewDirection(renderer, 0, 0, 1, 0, 1, 0)


def ViewNegativeZ(renderer):
    ViewDirection(renderer, 0, 0, -1, 0, 1, 0)


def ResetCam(renderer):
    renderer.ResetCamera()
    renderer.GetRenderWindow().Render()


def SetGridModel(renderer, model):
    actor = renderer.GetActors().GetLastActor()
    if model:
        actor.GetProperty().EdgeVisibilityOn()
    else:
        actor.GetProperty().EdgeVisibilityOff()
    renderer.GetRenderWindow().Render()


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


def addMeshTools(self, vtkwidget):
    q = QWidget()
    qhbox = QHBoxLayout()
    qhbox.addWidget(vtkwidget)
    q.setLayout(qhbox)
    qhbox.setContentsMargins(0, 0, 0, 0)
    qhbox.setSpacing(1)
    toobar = QToolBar()
    toobar.setOrientation(Qt.Vertical)

    x_1 = QAction(q)
    x_1.setIcon(QIcon(QPixmap(':/grid/img/grid/+X.png')))
    x_1.triggered.connect(lambda: ViewPositiveX(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    x_1.setToolTip('+X')

    x_2 = QAction(q)
    x_2.setIcon(QIcon(QPixmap(':/grid/img/grid/-X.png')))
    x_2.triggered.connect(lambda: ViewNegativeX(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    x_2.setToolTip('-X')

    y_1 = QAction(q)
    y_1.setIcon(QIcon(QPixmap(':/grid/img/grid/+Y.png')))
    y_1.triggered.connect(lambda: ViewPositiveY(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    y_1.setToolTip('+Y')

    y_2 = QAction(q)
    y_2.setIcon(QIcon(QPixmap(':/grid/img/grid/-Y.png')))
    y_2.triggered.connect(lambda: ViewNegativeY(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    y_2.setToolTip('-Y')

    z_1 = QAction(q)
    z_1.setIcon(QIcon(QPixmap(':/grid/img/grid/+Z.png')))
    z_1.triggered.connect(lambda: ViewPositiveZ(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    z_1.setToolTip('+Z')

    z_2 = QAction(q)
    z_2.setIcon(QIcon(QPixmap(':/grid/img/grid/-Z.png')))
    z_2.triggered.connect(lambda: ViewNegativeZ(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    z_2.setToolTip('-Z')

    model = QAction(q)
    model.setIcon(QIcon(QPixmap(':/grid/img/grid/NoBorder.png')))
    model.setToolTip('切换网格显示')
    model.setCheckable(True)
    model.setChecked(True)
    model.triggered.connect(
        lambda: SetGridModel(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer(), model.isChecked()))

    reset = QAction(q)
    reset.setIcon(QIcon(QPixmap(':/grid/img/grid/SetBorder.png')))
    reset.triggered.connect(lambda: ResetCam(vtkwidget.GetRenderWindow().GetRenderers().GetFirstRenderer()))
    reset.setToolTip('重置')

    toobar.addAction(x_1)
    toobar.addAction(x_2)
    toobar.addAction(y_1)
    toobar.addAction(y_2)
    toobar.addAction(z_1)
    toobar.addAction(z_2)
    toobar.addAction(model)
    toobar.addAction(reset)

    toobar.setStyleSheet("\
            QToolBar { background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255,255,255, 255), stop:1 rgba(255, 255, 255, 255)); spacing: 0px; } \
    		QToolBar QToolButton:hover { border: 1px solid #2c70a1; } \
    		QToolBar QToolButton:checked { border: 1px solid #328ac9; } \
            QToolBar::separator:vertical { background: yellow; margin-top: 2px; margin-bottom: 2px; border: 0px; height: 2px; }")
    qhbox.addWidget(toobar)
    return q


def solt_action_meshimport(self):
    action = self.form.sender()
    path, typle = QtWidgets.QFileDialog.getOpenFileName(self.form, '选择导入的网格文件', '.',
                                                        'Fluent Cas File(*.cas);;PLOT3D File(*.xyz)', )
    if typle == 'Fluent Cas File(*.cas)':
        r = vtk.vtkFLUENTReader()
        r.SetFileName(path)
        r.EnableAllCellArrays()
    elif typle == 'CGNS File(*.cgns)':
        r = vtk.vtkCGNSReader()
        r.SetFileName(path)
        r.EnableAllCellArrays()
    elif typle == 'PLOT3D File(*.xyz)':
        r = vtk.vtkMultiBlockPLOT3DReader()
        r.SetXYZFileName(path)
    else:
        return
    _, file_name = os.path.split(path)
    self.vtkWidget = QVTKRenderWindowInteractor(self.form)

    r.Update()
    g = vtk.vtkGeometryFilter()
    g.SetInputConnection(r.GetOutputPort())

    ##########################################################
    # 显示网格
    # MeshMapper = vtk.vtkCompositePolyDataMapper2()
    MeshMapper = vtk.vtkCompositePolyDataMapper()
    MeshMapper.SetInputConnection(g.GetOutputPort())
    MeshActor = vtk.vtkActor()
    MeshActor.SetMapper(MeshMapper)
    MeshProp = MeshActor.GetProperty()
    MeshProp.EdgeVisibilityOn()

    MeshRen = vtk.vtkRenderer()
    MeshRen.SetViewport(0.0, 0.0, 1.0, 1.0)
    MeshRen.GradientBackgroundOn()
    MeshRen.SetBackground(1, 1, 1)
    MeshRen.SetBackground2(0.4, 0.55, 0.75)
    MeshRen.AddActor(MeshActor)

    ##########################################################
    self.vtkWidget.GetRenderWindow().AddRenderer(MeshRen)

    iren = self.vtkWidget.GetRenderWindow().GetInteractor()
    iren.Initialize()

    iren.axes = MakeAxesActor()
    om = vtk.vtkOrientationMarkerWidget()
    om.SetOrientationMarker(iren.axes)
    om.SetInteractor(iren)
    om.EnabledOn()
    om.InteractiveOff()
    iren.om = om

    style = vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    q = self.addMeshTools(self.vtkWidget)

    self.mains["panel"].ui().tabWidget.addTab(q, QIcon(QPixmap(':/db/三维体分析692.svg')), file_name)
    currentindex = self.mains["panel"].ui().tabWidget.count() - 1
    self.mains['panel'].ui().tabWidget.setCurrentIndex(currentindex)

    mesh = QTreeWidgetItem(self.paras['szmn'].ui().mesh)
    mesh.flag = FLAG_MESH_LIST
    mesh._data = currentindex
    mesh.setText(0, file_name)
    mesh.setIcon(0, QIcon(QPixmap(':/db/三维体分析692.svg')))
