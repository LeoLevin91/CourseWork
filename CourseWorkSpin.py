# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CourseWorkGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(725, 602)
        MainWindow.setStyleSheet("background-color: #181818")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 50, 541, 41))
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 110, 601, 401))
        self.widget.setStyleSheet("background-color: #181818;")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 20, 271, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.spinBoxContainer = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.spinBoxContainer.setContentsMargins(0, 0, 0, 0)
        self.spinBoxContainer.setObjectName("spinBoxContainer")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_2.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_2.setMaximum(200.0)
        self.doubleSpinBox_2.setSingleStep(1.0)
        self.doubleSpinBox_2.setProperty("value", 8.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_1.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_1.setSingleStep(0.01)
        self.doubleSpinBox_1.setProperty("value", 0.01)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_3.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_3.setMaximum(9999.99)
        self.doubleSpinBox_3.setSingleStep(1.0)
        self.doubleSpinBox_3.setProperty("value", 30.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_3)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_5.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setSingleStep(0.001)
        self.doubleSpinBox_5.setProperty("value", 0.003)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_5)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_4.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_4.setSingleStep(0.001)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_4)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_6.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_6.setSingleStep(0.001)
        self.doubleSpinBox_6.setProperty("value", 0.11)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_6)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_7.setStyleSheet("background-color: #fff;")
        self.doubleSpinBox_7.setSingleStep(0.001)
        self.doubleSpinBox_7.setProperty("value", 1.65)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_7)
        self.intSpinBox_1_8 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.intSpinBox_1_8.setStyleSheet("background-color: #fff;")
        self.intSpinBox_1_8.setMaximum(1000)
        self.intSpinBox_1_8.setProperty("value", 100)
        self.intSpinBox_1_8.setDisplayIntegerBase(10)
        self.intSpinBox_1_8.setObjectName("intSpinBox_1_8")
        self.spinBoxContainer.addWidget(self.intSpinBox_1_8)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 287, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_1.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setStyleSheet("color: #fff;\n"
"font-size: 14px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.calculateButton = QtWidgets.QPushButton(self.widget)
        self.calculateButton.setGeometry(QtCore.QRect(210, 360, 121, 31))
        self.calculateButton.setStyleSheet("background-color: #1DB954;\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"font-size: 16px;\n"
"font-weight: 600;")
        self.calculateButton.setObjectName("calculateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # При нажати на кнопку происходит переход к методу расчета
        self.calculateButton.clicked.connect(self.buttonClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#c5c5c5;\">Петров, Борисов; группа: 6310, В:№34</span></p></body></html>"))
        self.label_1.setText(_translate("MainWindow", "Длинна стержня (l)"))
        self.label_2.setText(_translate("MainWindow", "Площадь сечения стержня (S)"))
        self.label_3.setText(_translate("MainWindow", "Момент времени (T)"))
        self.label_4.setText(_translate("MainWindow", "Коэффициент теплообмена (alpha)"))
        self.label_5.setText(_translate("MainWindow", "Температура окружающей среды (U0)"))
        self.label_6.setText(_translate("MainWindow", "Коэффициент теплопроводности (k)"))
        self.label_7.setText(_translate("MainWindow", "Коэффициент объемной темплоемкости (c)"))
        self.label_8.setText(_translate("MainWindow", "Колличество суммирований ряда (n)"))
        self.calculateButton.setText(_translate("MainWindow", "Расчет"))

    def buttonClicked(self):
        l = float(self.doubleSpinBox_2.value())
        print(l)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
