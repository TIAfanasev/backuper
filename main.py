import subprocess
import os
from datetime import date
import shutil
import time

def dumper(output_file):
    db_name = 'HIV'
    db_user = 'sa2'
    db_host = '192.168.27.1'
    password = '4100'

    # Установите переменную окружения PGPASSWORD
    env = os.environ.copy()
    env['PGPASSWORD'] = password

    # Команда для создания дампа с использованием пароля через аргумент input
    command = f'pg_dump -U {db_user} -h {db_host} -d {db_name} -f {output_file}'

    # Используйте subprocess.run для выполнения команды
    result = subprocess.run(command, shell=True, env=env, text=True, capture_output=True)

    # Проверьте код завершения
    if result.returncode == 0:
        print('Дамп успешно создан.')
    else:
        print(f'Ошибка при создании дампа: {result.stderr}')
    return result.returncode

if __name__ == '__main__':
    while True:
        dump_name = f'HIV-{date.today()}.dump'
        print('Началось создание дампа')
        res = dumper(dump_name)
        if not res:
            path_to = "\\\\DiskStation\Общедоступные файлы\Infosystem\BACKUPs"
            print('Началось копирование дампа')
            try:
                shutil.copy2(dump_name, path_to)
                print('Дамп скопирован')
            except Exception:
                print('Ошибка копирования.')
                sleep_time = 1800
            else:
                os.remove(dump_name)
                sleep_time = 86400
                print('Переход в спящий режим. До завтра!')
        else:
            print('Обосрался и спит')
            sleep_time = 1800
        time.sleep(sleep_time)