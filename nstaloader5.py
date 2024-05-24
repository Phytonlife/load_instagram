import tkinter as tk
from tkinter import ttk
import instaloader
import os
from time import sleep
from random import uniform

# Функция для скачивания фотографий
def download_photos():
    # Получить список имен пользователей и название папки
    usernames = usernames_entry.get().split(',')
    output_dir = folder_entry.get()

    # Инициализация Instaloader
    L = instaloader.Instaloader(download_pictures=True, download_videos=False, download_video_thumbnails=False,
                                download_geotags=False, download_comments=False, save_metadata=False,
                                post_metadata_txt_pattern="")

    # Создать папку, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Настроить папку для сохранения изображений
    L.dirname_pattern = output_dir

    # Скачивание постов для каждого пользователя
    for target_username in usernames:
        sleep(uniform(2, 5))
        profile = instaloader.Profile.from_username(L.context, target_username.strip())
        for post in profile.get_posts():
            sleep(uniform(0, 2))
            L.download_post(post, target=output_dir)


# Создание главного окна
root = tk.Tk()
root.title("Instagram Photo Downloader")

# Создание метки и поля ввода для имен пользователей
usernames_label = ttk.Label(root, text="Имена пользователей (разделите запятой):")
usernames_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
usernames_entry = ttk.Entry(root, width=40)
usernames_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Создание метки и поля ввода для названия папки
folder_label = ttk.Label(root, text="Название папки для сохранения:")
folder_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
folder_entry = ttk.Entry(root, width=40)
folder_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Создание кнопки для скачивания фотографий
download_button = ttk.Button(root, text="Скачать фотографии", command=download_photos)
download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Запуск главного цикла обработки событий
root.mainloop()
