""" Файл виртуального COM порта"""

import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM1'
ser.open()

while True:
    data = b'Hello, World!\n'  # замените на свои данные
    ser.write(data)
    time.sleep(1)
