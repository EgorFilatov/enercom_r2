# Form implementation generated from reading ui file 'D:\Python\Programs\enercom_r2\enercom_r2.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 841)
        MainWindow.setIconSize(QtCore.QSize(10, 10))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 130, 233, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.com_combo_box = QtWidgets.QComboBox(self.layoutWidget)
        self.com_combo_box.setObjectName("com_combo_box")
        self.horizontalLayout.addWidget(self.com_combo_box)
        self.turn_on_button = QtWidgets.QPushButton(self.layoutWidget)
        self.turn_on_button.setObjectName("turn_on_button")
        self.horizontalLayout.addWidget(self.turn_on_button)
        self.turn_off_button = QtWidgets.QPushButton(self.layoutWidget)
        self.turn_off_button.setObjectName("turn_off_button")
        self.horizontalLayout.addWidget(self.turn_off_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enercom R2 ????????????????????????"))
        self.turn_on_button.setText(_translate("MainWindow", "????????????????"))
        self.turn_off_button.setText(_translate("MainWindow", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
