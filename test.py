# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("weather forecast")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(320, 20, 151, 61))
        self.title.setObjectName("title")
        self.instruct = QtWidgets.QLabel(self.centralwidget)
        self.instruct.setGeometry(QtCore.QRect(310, 140, 191, 41))
        self.instruct.setObjectName("instruct")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(260, 210, 301, 28))
        self.input.setObjectName("input")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(350, 280, 104, 31))
        self.search.setObjectName("search")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(260, 340, 301, 171))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.search.clicked.connect(self.clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def clicked(self):
        city = self.input.text()
        api_address = 'c56eecac03b967a3cdba2bef2b2e26f3'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        complete_url = base_url + "appid=" + api_address + "&q=" + city + "&units=metric"
        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":
            y = x["main"]

            c_temp = y['temp']
            c_pressure = y['pressure']
            c_humidity = y['humidity']


            z = x["weather"]

            weather_description = z[0]["description"]
            self.output.setText(" Temperature = " +
              str(c_temp) + "°C" +
              "\n atmospheric pressure = " +
              str(c_pressure) + "hPa" +
              "\n humidity = " +
              str(c_humidity) + "%"+
              "\n description = " +
              str(weather_description))

        else:
            self.output.setText("city not found")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Weather Forecast"))
        self.instruct.setText(_translate("MainWindow", "Input name of the city"))
        self.search.setText(_translate("MainWindow", "search"))
        self.output.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

