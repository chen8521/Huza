from huza.icons.iconcore import IconListHandler
from huza.icons.img import image_dict

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    c = IconListHandler()
    c.add_img_list('dd', image_dict)
    dd = c.dd.And627
    print(dd)
