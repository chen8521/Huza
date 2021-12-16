# coding=utf-8
import os
from huza.base.mainwindow_run import MainWindowRun


class Extra:
    debug = None
    speed = None

    def __init__(self, debug=False, speed=1):
        self.debug = debug
        self.speed = speed


DEBUG = True
speed = 1000

if 'DEBUG_MODE' in os.environ:
    DEBUG = True
    speed = 100


def add_actions(obj):
    obj.addAction('showsetup', '设置面板', '显示/隐藏设置面板', checkable=True, icon=obj.icon_list.default.Adddata6)
    obj.addAction('showpara', '导航面板', '显示/隐藏导航面板', checkable=True, icon=obj.icon_list.default.cot550)
    obj.addAction('showinfo', '信息面板', '显示/隐藏信息面板', checkable=True, icon=obj.icon_list.default.bim439)
    obj.addAction('exit', '退出', '退出', icon=obj.icon_list.default.Stop37)
    obj.addAction('t1', 't1', icon=obj.icon_list.default.Unit220)
    obj.addAction('t2', 't2', icon=obj.icon_list.default.Zoom100)


def init_menu(obj):
    c = {'开始': [
        {'测试': [('t1', True), ('t2', True)]},
        {'关闭': [('exit', True)]}
    ],
        '视图': [
            {'视图控制': ['showsetup', 'showpara', 'showinfo']},
        ],
    }
    obj.init_menu(c)


if __name__ == '__main__':
    extra = Extra(debug=DEBUG, speed=speed)
    app = MainWindowRun(extra)
    app.set_window_logo(app.icon_list.default.Calculatehortestpath_grid_671)
    app.set_window_title('测试')
    add_actions(app)
    init_menu(app)
    app.run()
