# Решить задачи, которые не успели решить на семинаре.
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# Каждая группа включает файлы с несколькими расширениями. 
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
from pathlib import Path
import os


type_files = {'mp3': 'audio', 'mp4': 'video', 'jpg': 'img', 'png': 'img',
              'doc': 'text', 'txt': 'text', 'xls': 'table', 'xlsx': 'table',
              'avi': 'video'}



def move_to(path):
    file_name = str(path).split(os.sep)[-1]
    if file_name.split('.')[-1] in type_files:
        return file_name, type_files[file_name.split('.')[-1]]
    return file_name, None


def sort_files(directory):
    work_dir = Path.cwd() / directory

    for obj in work_dir.iterdir():
        file_name, file_move_to = move_to(obj)
        if file_move_to:
            direction = True if os.path.isdir(file_move_to) else False
            if not direction:
                Path(file_move_to).mkdir()
            os.replace(str(obj), os.path.join(os.getcwd(), file_move_to, file_name))


if __name__ == '__main__':
    print('''
Данный скрипт перемещает файлы с расширениями:
- mp3 в директорию ==> audio;
- mp4, avi в директорию ==> video;
- txt, doc в директорию ==> text;
- jpg, png в директорию ==> img;
- xls, xlsx в директорию ==> table.
''')
    sort_files('all_files')
    print('Перенмещение файлов окончено.')
