from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDockWidget


def init_docks(app):
    d1 = QDockWidget("1")
    d1.setMinimumSize(QSize(700, 200))
    d1.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

    d2 = QDockWidget("2")
    d2.setMinimumWidth(280)
    d2.setMinimumHeight(300)
    d2.setFeatures(QDockWidget.AllDockWidgetFeatures)

    d3 = QDockWidget("3")
    d3.setMinimumWidth(350)
    d3.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

    d4 = QDockWidget("4")
    d4.setMaximumHeight(400)
    d4.setFeatures(QDockWidget.AllDockWidgetFeatures)
    docks = {
        'main': d1,
        'para': d2,
        'setup': d3,
        'info': d4,
    }
    layout = [('add', 'left', 'para'),
              ('split', 'para', 'setup', 'h'),
              ('split', 'setup', 'main', 'h'),
              ('split', 'main', 'info', 'v'),
              ]
    app.init_docks(docks, layout)
