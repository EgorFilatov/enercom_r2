import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6 import QtCore
from PyQt6.QtCore import QIODevice
from PyQt6.QtCore import QIODeviceBase


Form, Window = uic.loadUiType("enercom_r2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

com = QSerialPort()
com.setBaudRate(115200)
com.setPortName('COM4')
#com.open(QIODevice.OpenModeFlag.ReadWrite)


available_com_ports_list = QSerialPortInfo.availablePorts()
available_com_ports_names = []

for port in available_com_ports_list:
    available_com_ports_names.append(port.portName())

print(available_com_ports_names)
form.com_combo_box.addItems(available_com_ports_names)


def combo_box_click():
    print("cheburek")


def com_port_open():
    #com.setPortName(form.com_combo_box.currentText())
    com.setPortName('COM4')
    com.open(QIODevice.OpenModeFlag.ReadWrite)


def com_port_close():
    com.close()


def com_read_data():
    rx = com.readAll()
    #rx_string = str(rx).replace('b', '').replace("'", '').split("\\")
    rx_string = str(rx).replace('b', '').replace("'", '')
    begining_index = rx_string.find('xaa')
    print(rx)
    #print('Начало:' + rx_string[begining_index:-1])


form.com_combo_box.currentIndexChanged.connect(combo_box_click)
form.turn_on_button.clicked.connect(com_port_open)
form.turn_off_button.clicked.connect(com_port_close)

com.readyRead.connect(com_read_data)

app.exec()
