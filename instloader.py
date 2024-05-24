import instaloader

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

# Скачивание постов
profile = instaloader.Profile.from_username(L.context, target_username)
for post in profile.get_posts():
    L.download_post(post, target=target_username)
