from PyQt5.QtWidgets import QLabel, QLineEdit
from loguru import logger

from huza.ribbon.RibbonButton import RibbonButton


def init_ribbon(self, ribbondata: dict):
    """
    c = {'开始': [
        {'测试': [('t1', True), ('t2', True)]},
        {'关闭': [('exit', True)]}
    ],
        '视图': [
            {'视图控制': ['showsetup', 'showpara', 'showinfo']},
        ],
    }

    :param self:
    :type self:
    :param ribbondata:
    :type ribbondata:
    :return:
    :rtype:
    """
    for tabname, tabdata in ribbondata.items():
        tab = self._ribbon.add_ribbon_tab(tabname)
        for pane_dict in tabdata:
            for pane_name, pane_data in pane_dict.items():
                pane = tab.add_ribbon_pane(pane_name)
                for ribbonbutton in pane_data:
                    if isinstance(ribbonbutton, list) or isinstance(ribbonbutton, tuple):
                        if len(ribbonbutton) == 1:
                            action_name, islagre = ribbonbutton, True
                        elif len(ribbonbutton) == 2:
                            action_name, islagre = ribbonbutton
                        else:
                            logger.warning(f'pane[{pane_name}]格式错误')
                            continue
                        if action_name not in self.actions:
                            raise Exception(f'Action [{action_name}] is not existed!')
                        pane.add_ribbon_widget(RibbonButton(self.form, self.actions[action_name], islagre))
                    elif isinstance(ribbonbutton, str):
                        action_name = ribbonbutton
                        pane.add_ribbon_widget(RibbonButton(self.form, self.actions[action_name], True))
