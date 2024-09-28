from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from PIL import Image
import os

# Путь к файлам (укажите папку с файлами)
directory_path = "/home/serj/dev/mts-link/chunks/"

# Путь к файлу с данными
input_txt = os.path.join(directory_path, "updates.txt")

# Парсим файл и извлекаем список с таймингами
def parse_file(input_txt, directory_path):
    entries = []
    video_file = None
    with open(input_txt, 'r') as file:
        for line in file:
            time_str, file_name = line.strip().split(': ')
            h, m, s = map(int, time_str.split(':'))
            time_in_seconds = h * 3600 + m * 60 + s
            full_path = os.path.join(directory_path, file_name)  # Формируем полный путь к файлу
            entries.append((time_in_seconds, full_path))
            if video_file is None and file_name.endswith('.mp4'):
                video_file = full_path  # Находим первый видеофайл
    return entries, video_file

# Извлекаем аудио из видео с помощью FFmpeg
def extract_audio(video_file, output_audio):
    try:
        ffmpeg_extract_audio(video_file, output_audio)
    except Exception as e:
        print(f"Ошибка при извлечении аудио: {e}")

# Создание слайдшоу с таймингами
def create_slideshow(entries):
    slides = []
    for i, entry in enumerate(entries):
        if entry[1].endswith('.jpg'):
            # Вычисляем время, на которое должно отображаться изображение
            start_time = entry[0]
            if i + 1 < len(entries):
                end_time = entries[i + 1][0]  # Время следующего изображения
            else:
                end_time = start_time + 5  # Последнее изображение отображается 5 секунд, если нет следующего таймера

            duration = end_time - start_time  # Длительность показа текущего изображения

            img_clip = ImageClip(entry[1]).set_duration(duration)
            img_clip = img_clip.set_start(start_time)
            slides.append(img_clip)
    return concatenate_videoclips(slides, method="compose")

# Объединение аудио и видео
def combine_audio_video(slideshow, audio_file, output_video):
    audio_clip = AudioFileClip(audio_file)
    slideshow = slideshow.set_audio(audio_clip)
    slideshow.write_videofile(output_video, fps=24)

# Главная функция
def main():
    output_audio = os.path.join(directory_path, "extracted_audio.mp3")
    output_video = os.path.join(directory_path, "final_slideshow.mp4")

    # Парсим файл и получаем список изображений и видеофайл
    entries, video_file = parse_file(input_txt, directory_path)

    # Проверка наличия видеофайла
    if video_file is None:
        print("Видео файл (.mp4) не найден в текстовом файле.")
        return

    # Извлекаем аудио
    extract_audio(video_file, output_audio)
    
    # Создаем слайдшоу с правильными таймингами
    slideshow = create_slideshow(entries)
    
    # Объединяем аудио и слайдшоу
    combine_audio_video(slideshow, output_audio, output_video)

if __name__ == "__main__":
    main()
