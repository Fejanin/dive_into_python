# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. 
#   При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. 
#   Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона 
#   [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
#   желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def create_new_name(added_name: str, num: str, old_file: str, new_file_extension: str, _slice: list) -> None:
    new_name = '.'.join(old_file.split('.')[:-1])[_slice[0]:_slice[1]]
    if new_name:
        new_name += '_' + added_name + '_' + num + '.' + new_file_extension
    else:
        new_name = added_name + '_' + num + '.' + new_file_extension
    return new_name


def rename_files(added_name: str, num: int, old_file_extension: str, new_file_extension: str, _slice: list) -> None:
    all_files = [obj for obj in os.listdir() if os.path.isfile(obj) and obj.split('.')[-1] == old_file_extension]
    n = 1
    d = 5
    for i in all_files:
        number = '0' * (num - len(str(n))) + str(n)
        n += 1
        new_name = create_new_name(added_name, number, i, new_file_extension, _slice)
        os.rename(i, new_name)
        
if __name__ == '__main__':
    rename_files('rename', 3, 'txt', 'bin', [0, 2])
