# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from src.main.python.widgets.FileSlotWidget import FileSlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(414, 300)
        Form.setMinimumSize(QSize(400, 300))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.browserFileBtn = QPushButton(Form)
        self.browserFileBtn.setObjectName(u"browserFileBtn")
        sizePolicy.setHeightForWidth(self.browserFileBtn.sizePolicy().hasHeightForWidth())
        self.browserFileBtn.setSizePolicy(sizePolicy)
        self.browserFileBtn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.browserFileBtn, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.fileSlotWidget = FileSlotWidget(Form)
        self.fileSlotWidget.setObjectName(u"fileSlotWidget")
        self.fileSlotWidget.setStyleSheet(u"border: 1px dashed #000000;\n"
"margin: 10px;")

        self.verticalLayout.addWidget(self.fileSlotWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"WPS\u4e66\u7b7e\u8f6c\u6362", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5c06xml\u683c\u5f0f\u7684\u6587\u4ef6\u8f6c\u5316\u4e3apdfdir\u53ef\u4ee5\u4f7f\u7528\u7684\u683c\u5f0f", None))
        self.browserFileBtn.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5c06\u6587\u4ef6\u62d6\u5165\u4e0b\u65b9\u6846\u4e2d", None))
    # retranslateUi

