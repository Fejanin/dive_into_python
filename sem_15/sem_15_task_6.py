'''
- Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
- Соберите информацию в виде объектов namedtuple
- Каждый объект хранит:
    - имя файла без расширения или названия каталога,
    - расширение, если это файл,
    - флаг каталога,
    - название родительского каталога.
- В процессе сбора сохраните данные в текстовом файле используя логирование.
'''

import argparse
import os
import re
import logging


class NamedTuple:
    def __init__(self, path_obj):
        self.path_obj = path_obj
        self.parant_dir, self.name = re.split('\\/', path_obj)[-2:]
        self.define_file_or_dir()
        logger.info('\t' + str(self))


    def define_file_or_dir(self):
        if os.path.isfile(self.path_obj):
            if '.' in self.name:
                self.name, self.extention = self.name.split('.')
            else:
                self.extention = '(!расширение не определено!)'
            self.is_dir = False
        else:
            self.extention = None
            self.is_dir = True


    def __str__(self):
        res = f'файлом с расширением {self.extention}'
        return f'''Создан объект: {self.name}. Является {"директорией" if self.is_dir else res}. Расположен в директории - {self.parant_dir}.'''
        
            


logging.basicConfig(level=logging.INFO, filename='task15_error.log')
logger = logging.getLogger(__name__)



parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('path', metavar='1', type=str, nargs='*', help='enter path')
find_dir = parser.parse_args().path[0]

# проверить, что указанная директория существует
logger.info(f'Получен путь - {find_dir}')

if os.path.exists(find_dir):
    all_obj_in_dir = os.listdir(find_dir)

    for name in all_obj_in_dir:
        new_path = os.path.join(find_dir, name)  # поставит "/" или "\" за нас
        print(NamedTuple(new_path))
else:
    print('Неверно указан путь.')
    logger.error(f'Путь {find_dir} не существует!')
logger.info(f'{"=" * 50}\n')
