# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteam.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 212)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -20, 401, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 50, 210, 22))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.team_name = QtWidgets.QLineEdit(self.frame)
        self.team_name.setGeometry(QtCore.QRect(90, 91, 221, 41))
        self.team_name.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name.setObjectName("team_name")
        self.savename = QtWidgets.QPushButton(self.frame)
        self.savename.setGeometry(QtCore.QRect(150, 160, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.savename.setFont(font)
        self.savename.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.savename.setObjectName("savename")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New Team"))
        self.label.setText(_translate("Dialog", "Create New Team"))
        self.team_name.setPlaceholderText(_translate("Dialog", "Enter team name"))
        self.savename.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

