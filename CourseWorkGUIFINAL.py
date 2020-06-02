# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CourseWorkGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(725, 602)
        MainWindow.setStyleSheet("background-color: #181818; color: #fff")
        #QMessageBox.setStyleSheet("color: #fff")

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

        self.doubleSpinBox_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_2.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_2.setText(str(8.0))
        #self.doubleSpinBox_2.setProperty("value", 8)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_2)

        self.doubleSpinBox_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_1.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_1.setText(str(0.01))
        #self.doubleSpinBox_1.setProperty("value", 0.01)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_1)

        self.doubleSpinBox_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_3.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_3.setText(str(30.0))
        #self.doubleSpinBox_3.setProperty("value", 30.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_3)

        self.doubleSpinBox_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_5.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_5.setText(str(0.003))
        #self.doubleSpinBox_5.setProperty("value", 0.003)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_5)

        self.doubleSpinBox_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_4.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_4.setText(str(0.00))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_4)

        self.doubleSpinBox_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_6.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_6.setText(str(0.11))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_6)

        self.doubleSpinBox_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_7.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_7.setText(str(1.65))
        #self.doubleSpinBox_7.setProperty("value", 1.65)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_7)

        self.doubleSpinBox_1_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.doubleSpinBox_1_8.setStyleSheet("background-color: #fff; color: #000")
        self.doubleSpinBox_1_8.setText(str(0.001))
        self.doubleSpinBox_1_8.setObjectName("doubleSpinBox_1_8")
        self.spinBoxContainer.addWidget(self.doubleSpinBox_1_8)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 287, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_1.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setStyleSheet("color: #fff; font-size: 14px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setStyleSheet("color: #fff; font-size: 14px;")
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
        self.label_8.setText(_translate("MainWindow", "Эпсилон (eps)"))
        self.calculateButton.setText(_translate("MainWindow", "Расчет"))


    def buttonClicked(self):
        str = ""
        try:
            l = float(self.doubleSpinBox_2.text())
            print("Длинна стержня: ", l)
            if l <= 0:
                str += "Длина стержня должна быть > 0\n"
        except:
            str += "Длина стержня введена неправильно\n"

        try:
            S = float(self.doubleSpinBox_1.text())
            print("Площадь поперечного сечения стержня: ", S)
            if S < 0:
                str += "Площадь поперечного сечения должна быть >= 0\n"
        except:
            str += "Площадь поперечного сечения введёна неправильно\n"

        try:
            T = float(self.doubleSpinBox_3.text())
            print("Момент времени: ", T)
            if T < 0:
                str += "Момент времени должен быть >= 0\n"
        except:
            str += "Момент времени введён неправильно\n"

        try:
            alpha = float(self.doubleSpinBox_5.text())
            print("Коэффициент теплообмена: ", alpha)
            if alpha <= 0:
                str += "Коэффициент теплообмена должен быть > 0\n"
        except:
            str += "Коэффициент теплообмена введён неправильно\n"

        try:
            u0 = float(self.doubleSpinBox_4.text())
            print("Температура окружающей среды", u0)
        except:
            str += "Температура окружающей среды введена неправильно\n"

        try:
            k = float(self.doubleSpinBox_6.text())
            print("Коэффициент теплопроводности: ", k)
            if k < 0:
                str += "Коэффициент теплопроводности должен быть > 0\n"
        except:
            str += "Коэффициент теплопроводности введён неправильно\n"

        try:
            c = float(self.doubleSpinBox_7.text())
            print("Коэффициент объемной теплоемкости: ", c)
            if c <= 0:
                str += "Коэффициент объёмной теплоёмкости должен быть > 0\n"
        except:
            str += "Коэффициент объёмной теплоёмкости введён неправильно\n"

        try:
            eps = float(self.doubleSpinBox_1_8.text())
            print("Погрешность: ", eps)
            if eps < 0:
                str += "Погрешность должна быть >= 0\n"
        except:
            str += "Погрешность введёна неправильно\n"


        def f_n(n):
            if n == 0:
                return 0.25
            return (-2 * np.sin(0.75 * np.pi * n)) / (np.pi * n)

        def v_x_t(n, c, k, l, x, t, s, alpha, u0):
            r = np.sqrt(s / np.pi)
            sum = 0
            for i in range(0, n):
                degree_exp = -(k * (np.pi ** 2) * (i ** 2) / ((l ** 2) * c) + 2 * alpha / (r * c))
                sum = sum + (f_n(i) / (c * degree_exp) * (np.exp(degree_exp * t) - 1)) * np.cos(np.pi * i * x / l)
            return sum + u0

        def show_plot(n, c, k, l, s, alpha, u0, t):
            x = np.linspace(0, l, 1000)
            v = []
            for arg in x:
                v.append(v_x_t(n, c, k, l, arg, t, s, alpha, u0))
            fig, ax = plt.subplots()
            ax.set_title(f'Распределение температуры в стержне при t = {t}')
            ax.plot(x, v)
            ax.set_ylabel(f'V(x, {t})')
            ax.set_xlabel('Длина стержня')
            ax.grid()
            plt.show()

        def find_n(l, k, eps):
            N = 1
            const = np.power(l, 2) / (k * np.power(np.pi, 3))
            eval = const  # Оценка ряда при N=1
            while (eval > eps):
                N += 1
                eval = const / np.power(N, 2)
            return N

        if len(str) != 0:
            QMessageBox.about(MainWindow, "Ошибка", str)
            # QMessageBox.setStyleSheet("color: #fff")
        else:
            N = find_n(l, k, eps)
            show_plot(N, c, k, l, S, alpha, u0, T)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
