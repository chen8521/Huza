

def ChageSetting(self, args):
    item = args
    if item.flag == FLAG_TLMX:
        self.setSetupView(FLAG_TLMX, item.text(0), Setting_TLMX_Form)
    elif item.flag == FLAG_DXLMX:
        self.setSetupView(FLAG_DXLMX, item.text(0), Setting_DXLMX_Form)
    elif item.flag == FLAG_JZTXSZ:
        self.setSetupView(FLAG_JZTXSZ, item.text(0), Setting_JZTXSZ_Form)
    elif item.flag == FLAG_JZZX:
        self.setSetupView(FLAG_JZZX, item.text(0), Setting_JZZX_Form)
    elif item.flag == FLAG_BJTJSZ:
        self.setSetupView(FLAG_BJTJSZ, item.text(0), Setting_BJTJSZ_Form)
    elif item.flag == FLAG_ZYMWZ:
        self.setSetupView(FLAG_ZYMWZ, item.text(0), Setting_ZYMWZ_Form)
    elif item.flag == FLAG_DWGSZ:
        self.setSetupView(FLAG_DWGSZ, item.text(0), Setting_DWGSZ_Form)
    elif item.flag == FLAG_RUN_LIST:
        self.setSetupView(FLAG_RUN_LIST, item.text(0), Setting_JSCS_Form)


def ImportMesh(self, args):
    item = args
    self.setSetupView(FLAG_IMPORTMESH,item.text(0), IMPORTMESH_Form)


def ChangeMesh(self, args):
    item = args
    if hasattr(item, 'flag') and item.flag == FLAG_MESH_LIST:
        index = item._data
        self.mains['panel'].ui().tabWidget.setCurrentIndex(index)
