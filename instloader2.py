import instaloader
import os
from time import sleep
from random import uniform

# Инициализация Instaloader
L = instaloader.Instaloader()

# Учетные данные (если нужен доступ к приватным аккаунтам)
# username = 'your_username'
# password = 'your_password'
#
# # Войти в систему (необязательно, если аккаунт публичный)
# L.login(username, password)

# Имя пользователя, чьи посты нужно скачать
target_username = 'asruamina3'

# Папка для сохранения изображений
output_dir = 'images'

# Создать папку, если она не существует
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Скачивание постов
profile = instaloader.Profile.from_username(L.context, target_username)
for post in profile.get_posts():
    sleep(uniform(0,2))
    # Сохранить изображения в указанную папку
    L.download_post(post, target=os.path.join(output_dir, target_username))
