""" Утилиты опроса COM портов и отправки данных"""
import serial


class PollingCom:
    """ Диспетчер контекста подключения к COM порту"""
    def __init__(self, configurations: dict):
        self.config = configurations
        self.real_port = None

    def __enter__(self):
        """ Подключается к заданному порту с заданной скоростью"""
        self.real_port = serial.Serial(**self.config)
        self.real_port.isOpen()
        return self.real_port

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.real_port.close()
