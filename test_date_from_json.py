import json
import time
import os

def process_updates(json_file):
    # Получаем путь к директории JSON файла
    directory = os.path.dirname(json_file)
    
    # Создаём имя выходного файла
    output_file = os.path.join(directory, 'updates.txt')
    
    # Очищаем файл перед записью (режим 'w' перезаписывает файл)
    with open(output_file, 'w') as output:
        pass  # Просто открываем файл в режиме записи, чтобы очистить его

    # Открываем и загружаем данные из JSON файла
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Открываем файл для добавления данных
    with open(output_file, 'a') as output:
        for update in data:  # Проходим по каждому элементу списка
            if 'data' in update and 'file' in update['data'] and 'relativeTime' in update:
                file_name = update['data']['file']
                relative_time = update['relativeTime']
                
               
                # Форматируем время как HH:MM:SS (убираем дату)
                readable_time = time.strftime('%H:%M:%S', time.gmtime(relative_time))
                
                # Записываем информацию в файл
                output.write(f"{readable_time}: {file_name}\n")

# Задайте путь к вашему JSON файлу
json_file_path = '/home/serj/dev/mts-link/downloads/Базовый онлайн-курс по MasterSCADA 4D. Занятие 1. 2024-09-16 09:56:06/script.json'  # Путь к вашему JSON файлу

process_updates(json_file_path)

