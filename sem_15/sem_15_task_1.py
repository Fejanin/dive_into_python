import logging


logging.basicConfig(level=logging.INFO, filename='task1_error.log')
logger = logging.getLogger(__name__)


def zero_devide(num_1, num_2):
    try:
        result = num_1 / num_2
        logger.info(f'Деление {num_1} на {num_2} прошло успешно. Результат - {result}.')
    except ZeroDivisionError as e:
        logger.error(f'Получили ошибку: {e}.\n\tПараметры: {num_1 = }, {num_2 = }.')
        result = float('inf') * (num_1 or 1)
    logger.info(f'Функция вернула знчение - {result}.\n')
    return result


print(zero_devide(4, 2))
print(zero_devide(4, 0))
print(zero_devide(8, 0.5))
print(zero_devide(0, 0))
print(zero_devide(1/2, 5.2))
print(zero_devide(-22, 0))
