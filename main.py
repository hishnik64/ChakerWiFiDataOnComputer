import subprocess
import time

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')

Wi_FI_list = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]

for Wi_FI in Wi_FI_list:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', Wi_FI, 'key=clear']).decode('cp866').split(
        '\n')
    results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]

    try:
        print(f'Имя сети: {Wi_FI}, Пароль:{results[0]}')
    except IndexError:
        print(f'Имя сети: {Wi_FI}, Пароль не найден!')
