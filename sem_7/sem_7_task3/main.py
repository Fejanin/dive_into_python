import my_lib as ml
from my_lib import renamed_files, sorted_files

if __name__ == '__main__':
    print(ml.NAME)
    print(f'''Из пакета my_lib были импортированы модули:
- renamed_files с встроенной функцией {renamed_files.rename_files.__name__}
- sorted_files с встроенной функцией {sorted_files.sort_files.__name__}.''')
    
