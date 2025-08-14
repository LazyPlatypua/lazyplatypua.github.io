import os
from PIL import Image, ImageOps

def add_border_to_images(root_folder):
    # Цвет рамки в формате RGB (#dddddd -> (221, 221, 221))
    border_color = (221, 221, 221)
    border_width = 1  # Ширина рамки в пикселях
    
    # Проходим по всем файлам и подпапкам в root_folder
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # Проверяем, является ли файл изображением
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(foldername, filename)
                try:
                    # Открываем изображение
                    with Image.open(file_path) as img:
                        # Добавляем рамку
                        bordered_img = ImageOps.expand(img, border=border_width, fill=border_color)
                        
                        # Сохраняем изображение (перезаписываем оригинал)
                        bordered_img.save(file_path)
                        print(f"Обработано: {file_path}")
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

if __name__ == "__main__":
    folder_path = input("Введите путь к папке с изображениями: ")
    if os.path.isdir(folder_path):
        add_border_to_images(folder_path)
        print("Обработка завершена!")
    else:
        print("Указанная папка не существует.")