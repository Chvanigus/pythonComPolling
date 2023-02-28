""" Файл настроек для проекта"""
import serial

SERIAL_CONFIG = {
    'port': 'COM1',
    'baudrate': 9600,
    'bytesize': 8,
    'timeout': 2,
    'stopbits': serial.STOPBITS_ONE
}

DB_CONFIG = {
    'host': '192.168.0.9',
    'user': 'geoadmin',
    'password': 'canopus',
    'database': 'gpgeo'
}
