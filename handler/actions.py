def init_actions(app):
    app.addAction('showsetup', '设置面板', '显示/隐藏设置面板', checkable=True, icon=app.icon_list.default.Adddata6)
    app.addAction('showpara', '导航面板', '显示/隐藏导航面板', checkable=True, icon=app.icon_list.default.cot550)
    app.addAction('showinfo', '信息面板', '显示/隐藏信息面板', checkable=True, icon=app.icon_list.default.bim439)
    app.addAction('exit', '退出', '退出', icon=app.icon_list.default.Stop37)
    app.addAction('t1', 't1', icon=app.icon_list.default.Unit220)
    app.addAction('t2', 't2', icon=app.icon_list.default.Zoom100)
    app.addAction('showicon', '显示图标', '显示图标', checkable=False, icon=app.icon_list.default.CMYKmode566)
