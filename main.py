import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt6 import QtCore
from PyQt6.QtCore import QIODevice
from PyQt6.QtCore import QIODeviceBase
import re


Form, Window = uic.loadUiType("enercom_r2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

com = QSerialPort()
com.setBaudRate(115200)

message = ''

available_com_ports_list = QSerialPortInfo.availablePorts()
available_com_ports_names = []

for port in available_com_ports_list:
    available_com_ports_names.append(port.portName())

print(available_com_ports_names)
form.com_combo_box.addItems(available_com_ports_names)


def combo_box_click():
    print("cheburek")


def com_port_open():
    com.setPortName(form.com_combo_box.currentText())
    #com.setPortName('COM4')
    com.open(QIODevice.OpenModeFlag.ReadWrite)


def com_port_close():
    com.close()


def com_read_data():
    rx = str(com.readAll().toHex()).replace('b', '').replace("'", '')
    global message
    message_full = ''
    convert_to_hex_flag = 0
    if rx[0] == '5' and rx[1] == '5':
        message_full = message
        convert_to_hex_flag = 1
        message = rx
    else:
        message = message + rx

    if convert_to_hex_flag == 1 and len(message_full) > 0:
        convert_to_hex_flag = 0
        message_full = re.findall('.{%s}' % 2, message_full)
        message_full_int = []
        #print(message_full)
        i = 0
        for el in message_full:
            message_full_int.append(int(el, 16))

        print(message_full_int)












    #rx_string = str(rx).replace('b', '').replace("'", '').split("\\")
    #rx_string = str(rx).replace('b', '').replace("'", '').replace("x", '')

    #if rx_string[0] == 'U':
    #    message_full = message
    #    message_full = message_full.split("\\")
    #    #c = '0' + message_full[1]
    #    if len(message_full) > 1:
    #        c = int(message_full[2], 16)
    #        print(message_full)
    #    message = rx_string
    #else:
    #    message = message + rx_string


form.com_combo_box.currentIndexChanged.connect(combo_box_click)
form.turn_on_button.clicked.connect(com_port_open)
form.turn_off_button.clicked.connect(com_port_close)

com.readyRead.connect(com_read_data)

app.exec()
