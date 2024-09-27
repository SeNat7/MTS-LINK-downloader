import subprocess

def combine_audio_video(video_file, audio_file, output_file, start_time):
    """
    Объединяет видео и аудио, начиная видео с определенного времени.
    
    :param video_file: Путь к файлу видео (.mp4)
    :param audio_file: Путь к файлу аудио (.mp4)
    :param output_file: Путь к выходному файлу
    :param start_time: Время начала видео (в формате 'HH:MM:SS')
    """
    # Команда ffmpeg для объединения аудио и видео
    command = [
        'ffmpeg',
        '-i', video_file,              # Входное видео
        '-i', audio_file,              # Входное аудио
        '-ss', start_time,             # Время начала воспроизведения видео
        '-c:v', 'copy',                # Копируем видео
        '-c:a', 'aac',                 # Кодек для аудио
        output_file                    # Выходной файл
    ]
    
    # Выполнение команды
    subprocess.run(command, check=True)

# Пример использования
video_path = '/home/serj/test_downloader/black_video.mp4'   # Замените на ваш путь к видео
audio_path = '/home/serj/webinar-downloader/downloads/Базовый онлайн-курс по MasterSCADA 4D. Занятие 2. 2024-09-18 11:58:38/chunks/8db23c2d0f5c0dd944bfd7df6ad2dbda231e51baf7b726f1fb430c66d62.mp4'     # Замените на ваш путь к аудио
output_path = '/home/serj/webinar-downloader/downloads/Базовый онлайн-курс по MasterSCADA 4D. Занятие 2. 2024-09-18 11:58:38/output.mp4'   # Замените на ваш путь к выходному файлу
start_time = '00:20:55'               # Время начала (например, 10 секунд)

combine_audio_video(video_path, audio_path, output_path, start_time)

