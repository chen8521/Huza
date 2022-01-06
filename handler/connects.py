from uis.navigate import NaviGate_Form
from uis.showicon import ShowIcon_Form


def init_connect(self):
    exit = self.get_action('exit')
    exit.triggered.connect(self.mainwindow.close)

    showpara = self.get_action('showpara')
    para_dock = self.get_dock('para')
    para_dock.visibilityChanged.connect(showpara.setChecked)
    showpara.triggered.connect(para_dock.setVisible)

    showinfo = self.get_action('showinfo')
    info_dock = self.get_dock('info')
    info_dock.visibilityChanged.connect(showinfo.setChecked)
    showinfo.triggered.connect(info_dock.setVisible)

    t1 = self.get_action('t1')

    def navi():
        self.set_dock_view('navi', '功能', 'para', NaviGate_Form)

    t1.triggered.connect(navi)

    showicon = self.get_action('showicon')

    def showicon_tri():
        self.set_dock_view('icon', '图标', 'main', ShowIcon_Form)
    showicon.triggered.connect(showicon_tri)