""" Скрипт для весовой"""

import logging
import socket

import settings
from utils import PollingCom

logger = logging.getLogger('__name__')


if __name__ == '__main__':
    # Активируем сокет для передачи данных
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    # Слушаем COM порт в бесконечном цикле
    while True:
        with PollingCom(settings.SERIAL_CONFIG) as ser:
            print(ser.readline())
            c, addr = s.accept()
            # Как только произошло открытие сокета - данные из COM порта отправляются на заданную машину
            print('Открыто соединение с:', addr)
            data = ser.readline()
            c.send(data)
            c.close()


