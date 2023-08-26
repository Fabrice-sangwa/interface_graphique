# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(366, 463)
        self.actiongg = QAction(Form)
        self.actiongg.setObjectName(u"actiongg")
        self.actiongg.setMenuRole(QAction.NoRole)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-3, 0, 371, 451))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(40, 50))

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(48, 48))
        self.pushButton_2.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(48, 48))
        self.pushButton_14.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_14, 4, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QSize(48, 48))
        self.pushButton_17.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_17, 6, 0, 1, 2)

        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QSize(48, 48))
        self.pushButton_19.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_19, 6, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(48, 48))
        self.pushButton_3.setStyleSheet(u"color : rgb(255, 135, 146); \n"
"font-style: bold; ")
        self.pushButton_3.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(48, 48))
        self.pushButton_16.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_16, 4, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(48, 48))
        self.pushButton_9.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(48, 48))
        self.pushButton_12.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_12, 3, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(48, 48))
        self.pushButton_5.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(48, 48))
        self.pushButton_11.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(48, 48))
        self.pushButton_7.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(48, 48))
        self.pushButton_6.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(48, 48))
        self.pushButton_10.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(48, 48))
        self.pushButton_8.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_8, 2, 3, 1, 1)

        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QSize(48, 48))
        self.pushButton_13.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_13, 4, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(48, 48))
        self.pushButton_15.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_15, 4, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMinimumSize(QSize(48, 48))
        self.pushButton_20.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_20, 6, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.actiongg.setText(QCoreApplication.translate("Form", u"gg", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi
