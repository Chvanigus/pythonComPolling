""" Функции взаимодействия с базой данных"""

import psycopg2
import logging
import settings

logger = logging.getLogger('__name__')
db_config = settings.DB_CONFIG


class DBConnector:
    """ Диспетчер контекста для подключения к базе данных.
        Параметры подключения передаются через словарь
    """

    def __init__(self, config_dict: dict) -> None:
        self.configuration = config_dict

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.Error as e:
            logger.critical(f'Ошибка при подключении к базе данных. Ошибка: {e}')

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def check_reg_status(telegram_id: int) -> bool:
    """ Проверка статуса подтверждения регистрации пользователя

    :param telegram_id:
        Идентификатор пользователя в telegram
    :return:
        Если у пользователя есть подтверждение регистрации - возвращается True
    """
    try:
        with DBConnector(db_config) as cur:
            sql = f'SELECT regcheck FROM public."TelegramBot" WHERE telegram_id in (%s)'
            cur.execute(sql, (telegram_id,))
            status = cur.fetchall()
            return status[0][0]
    except IndexError as e:
        logger.critical(
            f'Невозможно проверить статус регистрации пользователя. Ошибка: {e}')