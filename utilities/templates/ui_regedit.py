# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regedit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(364, 59)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.b3 = QtWidgets.QCheckBox(Frame)
        self.b3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 0, 5, 1, 1)
        self.b2 = QtWidgets.QCheckBox(Frame)
        self.b2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 0, 6, 1, 1)
        self.regName = QtWidgets.QComboBox(Frame)
        self.regName.setEditable(True)
        self.regName.setMaxVisibleItems(15)
        self.regName.setObjectName("regName")
        self.gridLayout.addWidget(self.regName, 0, 0, 1, 1)
        self.b1 = QtWidgets.QCheckBox(Frame)
        self.b1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 0, 7, 1, 1)
        self.b0 = QtWidgets.QCheckBox(Frame)
        self.b0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b0.setText("")
        self.b0.setObjectName("b0")
        self.gridLayout.addWidget(self.b0, 0, 8, 1, 1)
        self.b5 = QtWidgets.QCheckBox(Frame)
        self.b5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 0, 3, 1, 1)
        self.valueLabel = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.valueLabel.setFont(font)
        self.valueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.valueLabel.setObjectName("valueLabel")
        self.gridLayout.addWidget(self.valueLabel, 1, 0, 1, 1)
        self.b7 = QtWidgets.QCheckBox(Frame)
        self.b7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b7.setStyleSheet("")
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 0, 1, 1, 1)
        self.b4 = QtWidgets.QCheckBox(Frame)
        self.b4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 0, 4, 1, 1)
        self.b6 = QtWidgets.QCheckBox(Frame)
        self.b6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 0, 2, 1, 1)
        self.l7 = QtWidgets.QLabel(Frame)
        self.l7.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l7.setObjectName("l7")
        self.gridLayout.addWidget(self.l7, 1, 1, 1, 1)
        self.l6 = QtWidgets.QLabel(Frame)
        self.l6.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l6.setObjectName("l6")
        self.gridLayout.addWidget(self.l6, 1, 2, 1, 1)
        self.l5 = QtWidgets.QLabel(Frame)
        self.l5.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l5.setObjectName("l5")
        self.gridLayout.addWidget(self.l5, 1, 3, 1, 1)
        self.l4 = QtWidgets.QLabel(Frame)
        self.l4.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l4.setObjectName("l4")
        self.gridLayout.addWidget(self.l4, 1, 4, 1, 1)
        self.l3 = QtWidgets.QLabel(Frame)
        self.l3.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 1, 5, 1, 1)
        self.l2 = QtWidgets.QLabel(Frame)
        self.l2.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 1, 6, 1, 1)
        self.l1 = QtWidgets.QLabel(Frame)
        self.l1.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 1, 7, 1, 1)
        self.l0 = QtWidgets.QLabel(Frame)
        self.l0.setObjectName("l0")
        self.gridLayout.addWidget(self.l0, 1, 8, 1, 1)
        self.typeLabel = QtWidgets.QLabel(Frame)
        self.typeLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.typeLabel.setProperty("clickable", True)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 0, 9, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/control/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 9, 1, 1)

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(Frame.execute)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.valueLabel.setText(_translate("Frame", "0"))
        self.l7.setText(_translate("Frame", "7"))
        self.l6.setText(_translate("Frame", "6"))
        self.l5.setText(_translate("Frame", "5"))
        self.l4.setText(_translate("Frame", "4"))
        self.l3.setText(_translate("Frame", "3"))
        self.l2.setText(_translate("Frame", "2"))
        self.l1.setText(_translate("Frame", "1"))
        self.l0.setText(_translate("Frame", "0"))
        self.typeLabel.setText(_translate("Frame", "↑READ"))

from . import res_rc
