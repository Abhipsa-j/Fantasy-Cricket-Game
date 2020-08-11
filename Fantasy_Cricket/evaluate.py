# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from scoreboard import Ui_Dialog as Score  #Score window
import sqlite3
match= sqlite3.connect("cricket_db.db")
matchcur=match.cursor()


class Ui_evaluate_team(object):
    def __init__(self):  #initialising score window
        self.scoreDialog = QtWidgets.QMainWindow()
        self.score_screen = Score()
        self.score_screen.setupUi(self.scoreDialog)


    
    def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(634, 504)
        evaluate_team.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setGeometry(QtCore.QRect(90, 20, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cb_selectteam = QtWidgets.QComboBox(evaluate_team)
        self.cb_selectteam.setGeometry(QtCore.QRect(90, 70, 141, 21))
        self.cb_selectteam.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 10pt \"Century Gothic\";")
        self.cb_selectteam.setObjectName("cb_selectteam")
        self.cb_selectteam.addItem("")
        self.cb_selectmatch = QtWidgets.QComboBox(evaluate_team)
        self.cb_selectmatch.setEnabled(True)
        self.cb_selectmatch.setGeometry(QtCore.QRect(360, 70, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.cb_selectmatch.setFont(font)
        self.cb_selectmatch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 11pt \"Century Gothic\";")
        self.cb_selectmatch.setObjectName("cb_selectmatch")
        self.cb_selectmatch.addItem("")
        self.cb_selectmatch.addItem("")
        self.line = QtWidgets.QFrame(evaluate_team)
        self.line.setGeometry(QtCore.QRect(40, 95, 551, 41))
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(evaluate_team)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(evaluate_team)
        self.label_3.setGeometry(QtCore.QRect(350, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.calcscore_btn = QtWidgets.QPushButton(evaluate_team)
        self.calcscore_btn.setEnabled(True)
        self.calcscore_btn.setGeometry(QtCore.QRect(240, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.calcscore_btn.setFont(font)
        self.calcscore_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calcscore_btn.setAutoDefault(False)
        self.calcscore_btn.setObjectName("calcscore_btn")
        self.lw_players = QtWidgets.QListWidget(evaluate_team)
        self.lw_players.setGeometry(QtCore.QRect(80, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw_players.setFont(font)
        self.lw_players.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lw_players.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_players.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.lw_players.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lw_players.setObjectName("lw_players")
        self.lw_scores = QtWidgets.QListWidget(evaluate_team)
        self.lw_scores.setGeometry(QtCore.QRect(340, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw_scores.setFont(font)
        self.lw_scores.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lw_scores.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lw_scores.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lw_scores.setObjectName("lw_scores")

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)

        self.calcscore_btn.clicked.connect(self.final_score)
        selected_team = self.cb_selectteam.currentText()

        self.changedname(selected_team)
        self.cb_selectteam.currentTextChanged.connect(self.changedname)
        

    def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Dialog"))
        self.label.setText(_translate("evaluate_team", "Evaluate the Performance of your Fantasy Team"))
        self.cb_selectteam.setCurrentText(_translate("evaluate_team", "Select team"))
        self.cb_selectteam.setItemText(0, _translate("evaluate_team", "Select team"))
        self.cb_selectmatch.setItemText(0, _translate("evaluate_team", "select match"))
        self.cb_selectmatch.setItemText(1, _translate("evaluate_team", "Match1"))
        self.label_2.setText(_translate("evaluate_team", "Players"))
        self.label_3.setText(_translate("evaluate_team", "Points"))
        self.calcscore_btn.setStatusTip(_translate("evaluate_team", "calculating score"))
        self.calcscore_btn.setText(_translate("evaluate_team", "Calculate Score"))
        x = matchcur.execute("SELECT  DISTINCT name from teams;")
        team = x.fetchall()
        for i in team:
            self.cb_selectteam.addItem(i[0])
    def changedname(self, t):
        self.lw_players.clear()
        self.lw_scores.clear()
        y = matchcur.execute("SELECT players from teams WHERE name='" + t + "';")
        player = y.fetchall()
        
        # print('player',player)
        for j in player:
            self.lw_players.addItem(j[0])
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
        for k in value:
            self.lw_scores.addItem(str(k[0]))


    def final_score(self):
        total_score=0
        t=self.cb_selectteam.currentText()   # current teamname
        # print(t)
        z = matchcur.execute("SELECT value from teams WHERE name='" + t + "';")
        value = z.fetchall()
       
        # print('value', value)
        for k in value:
            total_score+=k[0]
        self.score_screen.finalscore.setText(str(total_score))  # opening score dialog box and setting final score
        self.scoreDialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QDialog()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())
