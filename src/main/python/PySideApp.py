from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
import sys
import xml.etree.ElementTree as ET

from src.main.python.view.Form import Ui_Form


class PdfSide(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initSignal()

    def initSignal(self):
        self.browserFileBtn.clicked.connect(self.browserFileBtnClicked)
        self.fileSlotWidget.signal.connect(self.parseXmlToFile)

    @Slot()
    def browserFileBtnClicked(self):
        print('browserFileBtnClicked')
        filename = QFileDialog.getOpenFileName(self)
        self.parseXmlToFile(filename[0])

    @Slot(str)
    def parseXmlToFile(self, filename):
        """
        使用ElementTree解析xml文件，将它转化为pdfdir可识别的内容
        :param filename: xml文件路径
        :return: None
        """
        tree = ET.parse(filename)
        root = tree.getroot()

        # 打印根节点标签
        print(f"Root element: {root.tag}")

        res = []
        self.recur(root, res)
        with open(filename.split('.')[0] + '_new.xml', 'w') as f:
            for i in res:
                f.write(i + '\n')

        print('done')

    def recur(self, root, res):
        """
        遍历xml树：root
        将节点名称为ITEM的节点存放在res中
        :param root xml树
        :param res list，用于存放结果
        :return None
        """
        for child in root:
            print(f"Tag: {child.tag}, Attributes: {child.attrib}")
            if child.tag == 'ITEM':
                item = ''
                item += child.attrib.get('NAME')
                item += ' '
                item += child.attrib.get('PAGE')
                res.append(item)
                self.recur(child, res)


def createWindow():
    app = QApplication(sys.argv)
    w = PdfSide()
    w.show()
    app.exec()
