def init_menu(app):
    menu = {'开始': [
        {'测试': [('t1', True), ('t2', True), ('t3', True, True)]},
        {'关闭': [('exit', True)]}
    ],
        '视图': [
            {'视图控制': ['showsetup', 'showpara', 'showinfo']},
        ],
        '帮助': [
            {'图标': ['showicon']}
        ]
    }
    app.init_menu(menu)
