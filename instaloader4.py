import instaloader
import os
from time import sleep
from random import uniform
# Инициализация Instaloader
L = instaloader.Instaloader(download_pictures=True, download_videos=False, download_video_thumbnails=False,
                            download_geotags=False, download_comments=False, save_metadata=False, post_metadata_txt_pattern="")

# Учетные данные (если нужен доступ к приватным аккаунтам)
# username = 'your_username'
# password = 'your_password'
#
# # Войти в систему (необязательно, если аккаунт публичный)
# L.login(username, password)

# Имя пользователя, чьи посты нужно скачать
target_username = 'asruamina3'

target_usernames = ['user1', 'user2', 'user3']
# Папка для сохранения изображений
output_dir = 'images'

# Создать папку, если она не существует
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Настроить папку для сохранения изображений
L.dirname_pattern = output_dir

# Скачивание постов

for target_username in target_usernames:
    sleep(uniform(2, 5))
    profile = instaloader.Profile.from_username(L.context, target_username)
    for post in profile.get_posts():
        sleep(uniform(0, 2))
        L.download_post(post, target=output_dir)


