# coding=utf-8
import os
from huza.util.buildui import build_uidir


class Extra:
    debug = None

    def __init__(self, debug=False):
        self.debug = debug


DEBUG = True
if 'DEBUG_MODE' in os.environ:
    DEBUG = True

if DEBUG:
    build_uidir('ui_file', 'auto_ui')

if __name__ == '__main__':
    from huza.base.mainwindow_run import MainWindowRun
    from handler import *

    extra = Extra(debug=DEBUG)
    app = MainWindowRun(extra)
    app.set_window_logo(app.icon_list.default.Analysisprocess517)
    app.set_window_title('测试')
    app.set_init_actions_func(init_actions)
    app.set_init_menu_func(init_menu)
    app.set_init_docks_func(init_docks)
    app.set_init_connect_func(init_connect)
    app.set_init_signal_func(init_signal)
    app.set_close_func(lambda s: print(s))
    app.set_close_info('test', 'test')
    app.set_splash_pic(app.icon_list.default.get_picmap('splash'))
    app.run()
