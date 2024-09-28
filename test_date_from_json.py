import json
import time
import os

def process_updates_in_directory(directory):
    # Проходим по каждому файлу и подкаталогам в директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Если найден файл с расширением .json
            if file.endswith('.json'):
                json_file = os.path.join(root, file)
                
                # Создаём имя выходного файла
                output_file = os.path.join(root, 'updates.txt')
                
                # Очищаем файл перед записью (режим 'w' перезаписывает файл)
                with open(output_file, 'w') as output:
                    pass  # Просто открываем файл в режиме записи, чтобы очистить его
                
                # Открываем и загружаем данные из JSON файла
                with open(json_file, 'r') as json_data_file:
                    data = json.load(json_data_file)
                
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

# Путь к директории downloads
downloads_directory = '/home/serj/dev/mts-link/downloads'  # Путь к вашей папке downloads

# Запускаем обработку всех папок в директории
process_updates_in_directory(downloads_directory)

