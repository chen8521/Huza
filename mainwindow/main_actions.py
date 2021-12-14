from util.navigationtool import MyNavigationToolbar2QT
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


def bind_action_slot(self, action_name, action_slot):
    self.actions[action_name].triggered.connect(action_slot)


def connectAction(self):
    _ = MyNavigationToolbar2QT

    self.actions["showpara"].triggered.connect(self.docks["para"].setVisible)
    self.actions["showsetup"].triggered.connect(self.docks["setup"].setVisible)
    self.actions["showinfo"].triggered.connect(self.docks["info"].setVisible)
    self.actions["exit"].triggered.connect(self.form.close)
    self.actions['help-version'].triggered.connect(self.solt_action_help_version)
    self.actions["help-about"].triggered.connect(self.solt_action_help_about)
    self.actions["help-doc"].triggered.connect(self.solt_action_help_doc)
    self.actions["coordinate_textedit"].triggered.connect(self.solt_action_coordinate_textedit)
    self.actions['coordinate_legend'].triggered.connect(self.solt_action_coordinate_legend)
    self.actions['coordinate_zoom_reset'].triggered.connect(self.solt_action_coordinate_zoom_reset)
    self.actions['coordinate_zoom'].triggered.connect(self.solt_action_coordinate_zoom)
    self.actions['coordinate_move'].triggered.connect(self.solt_action_coordinate_move)
    self.actions['coordinate_save'].triggered.connect(self.solt_action_coordinate_save)
    self.actions['coordinate_set'].triggered.connect(self.solt_action_coordinate_set)
    self.actions['gendemo'].triggered.connect(self.solt_action_gendemo)

    bind_action_slot(self, 'szmn', self.solt_action_szmn)
    bind_action_slot(self, 'importmesh', self.solt_action_meshimport)


def createActions(self):
    def createAct(text, tip=None, shortcut=None, iconimg=None, checkable=False, slot=None, myactionname=None,
                  enable=True):
        action = QAction(self.tr(text), self.form)
        if iconimg is not None:
            action.setIcon(QIcon(iconimg))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            tip = self.tr(tip)
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if checkable:
            action.setCheckable(True)
        if slot is not None:
            action.triggered.connect(slot)
        if myactionname is not None:
            action.myactionname = myactionname
        action.setEnabled(enable)
        return action

    self.actions["szmn"] = createAct('潜射过程数值模拟',
                                     self.tr("潜射过程数值模拟"),
                                     None,
                                     ':/db/浏览771.svg',
                                     myactionname='szmn'
                                     )

    self.actions["importmesh"] = createAct('网格导入',
                                           self.tr("网格导入"),
                                           None,
                                           ':/db/三维体分析692.svg',
                                           myactionname='importmesh',
                                           enable=False
                                           )

    self.actions["exit"] = createAct('退出',
                                     "退出程序",
                                     None,
                                     ':/db/乘596.svg')

    self.actions["analyse_heatmap_result_pred"] = createAct(self.tr("热流预测"),
                                                            self.tr("热流预测"),
                                                            None,
                                                            ':/db/热力图254.svg',
                                                            myactionname='result_rmse')

    self.actions["analyse_compare_heatflux"] = createAct(self.tr("热流结果对比"),
                                                         self.tr("热流结果对比"),
                                                         None,
                                                         ':/db/热力图254.svg',
                                                         myactionname='result_rmse')

    self.actions["analyse_compare_sim_test"] = createAct(self.tr("仿真与试验对比"),
                                                         self.tr("仿真与试验对比"),
                                                         None,
                                                         ':/db/聚类分布138.svg',
                                                         myactionname='result_rmse')

    self.actions["coordinate_textedit"] = createAct(self.tr("坐标文本设置"),
                                                    self.tr("设置横、纵坐标的显示文本"),
                                                    None,
                                                    ':/db/固定大小271.svg',
                                                    enable=True,
                                                    myactionname='coordinate_textedit'
                                                    )

    self.actions["coordinate_legend"] = createAct(self.tr("图例显示"),
                                                  self.tr("显示/隐藏坐标图例"),
                                                  None,
                                                  ':/db/统计图105.svg',
                                                  enable=True,
                                                  checkable=True
                                                  )

    self.actions["coordinate_log"] = createAct(self.tr("对数坐标"),
                                               self.tr("是否设置为对数坐标系"),
                                               None,
                                               ':/db/log552.svg',
                                               enable=True
                                               )

    self.actions["coordinate_set"] = createAct(self.tr("坐标样式设置"),
                                               self.tr("设置坐标系颜色、大小、标记等样式"),
                                               None,
                                               ':/db/设置格网数据91.svg',
                                               enable=True
                                               )

    self.actions["coordinate_zoom"] = createAct(self.tr("缩放"),
                                                self.tr("缩放坐标系"),
                                                None,
                                                ':/db/缩放235.svg',
                                                enable=True,
                                                checkable=True
                                                )

    self.actions["coordinate_zoom_reset"] = createAct(self.tr("恢复"),
                                                      self.tr("恢复坐标系"),
                                                      None,
                                                      ':/db/恢复默认参数设置543.svg',
                                                      enable=True
                                                      )
    self.actions["coordinate_move"] = createAct(self.tr("移动"),
                                                self.tr("移动坐标系"),
                                                None,
                                                ':/db/统计移动符号253.svg',
                                                enable=True,
                                                checkable=True
                                                )

    self.actions["coordinate_save"] = createAct(self.tr("绘图保存"),
                                                self.tr("绘图保存"),
                                                None,
                                                ':/db/保存57.svg',
                                                enable=True
                                                )

    self.actions["setting_local"] = createAct(self.tr("本地数据库设置"),
                                              self.tr("本地数据库设置"),
                                              None,
                                              ':/db/文件型118.svg',
                                              enable=True
                                              )
    self.actions["setting_postgres"] = createAct(self.tr("远程数据库设置"),
                                                 self.tr("远程数据库设置"),
                                                 None,
                                                 ':/db/Web型125.svg',
                                                 enable=True
                                                 )

    self.actions["setting_localfile"] = createAct(self.tr("本地文件系统"),
                                                  self.tr("本地文件系统"),
                                                  None,
                                                  ':/db/vectortext573.svg',
                                                  enable=True
                                                  )

    self.actions["setting_ftp"] = createAct(self.tr("FTP文件系统"),
                                            self.tr("FTP文件系统"),
                                            None,
                                            ':/db/ftp目录810.svg',
                                            enable=True
                                            )
    self.actions["setting_http"] = createAct(self.tr("HTTP文件系统"),
                                             self.tr("HTTP文件系统"),
                                             None,
                                             ':/db/选择漫游306.svg',
                                             enable=True
                                             )

    self.actions["help-about"] = createAct(self.tr("关于"),
                                           self.tr("关于本软件"),
                                           None,
                                           ':/db/信息查询75.svg',
                                           enable=True
                                           )

    self.actions["help-doc"] = createAct(self.tr("帮助手册"),
                                         self.tr("查看帮助手册"),
                                         None,
                                         ':/db/帮助776.svg',
                                         enable=True
                                         )
    self.actions["help-version"] = createAct(self.tr("版本更新日志"),
                                             self.tr("查看版本更新日志"),
                                             None,
                                             ':/db/显示所有记录515.svg'
                                             )
    self.actions["gendemo"] = createAct(self.tr("绘图案例"),
                                        self.tr("绘图案例"),
                                        None,
                                        ':/db/模型处理174.svg',
                                        myactionname='gendemo'
                                        )


    self.actions["showsetup"] = createAct(self.tr("设置面板"),
                                          self.tr("显示/隐藏设置面板"),
                                          None,
                                          ":/db/标绘图层控制器51.svg",
                                          checkable=True)

    self.actions["showpara"] = createAct(self.tr("导航面板"),
                                         self.tr("显示/隐藏导航面板"),
                                         None,
                                         ":/db/等级图652.svg",
                                         checkable=True)

    self.actions["showinfo"] = createAct(self.tr("信息面板"),
                                         self.tr("显示/隐藏信息面板"),
                                         None,
                                         ":/db/显示所有记录515.svg",
                                         checkable=True)







