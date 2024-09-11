from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
import sys
import xml.etree.ElementTree as ET

from src.main.python.view.Form import Ui_Form


class PdfSide(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.res = []
        self.setupUi(self)
        self.initSignal()

    def initSignal(self):
        self.browserFileBtn.clicked.connect(self.browserFileBtnClicked)

    @Slot()
    def browserFileBtnClicked(self):
        print('browserFileBtnClicked')
        filename = QFileDialog.getOpenFileName(self)

        tree = ET.parse(filename[0])
        root = tree.getroot()

        # 打印根节点标签
        print(f"Root element: {root.tag}")

        self.recur(root)

        with open(filename[0].split('.')[0] + '_new.xml', 'w') as f:
            for i in self.res:
                f.write(i + '\n')

        self.res = []
        print('done')

    def recur(self, root):
        # 遍历XML文件中的所有子元素
        for child in root:
            print(f"Tag: {child.tag}, Attributes: {child.attrib}")
            if child.tag == 'ITEM':
                item = ''
                item += child.attrib.get('NAME')
                item += ' '
                item += child.attrib.get('PAGE')
                self.res.append(item)
                self.recur(child)


def createWindow():
    app = QApplication(sys.argv)
    w = PdfSide()
    w.show()
    app.exec()