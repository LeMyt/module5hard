import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        #print('Вход')
        for user in self.users:
            if user.nickname == nickname and user.password_hash == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                #self.current_user = self.nickname
                return True
        return False

    def register(self, nickname, password, age):
        existing_user = next((user for user in self.users if user.nickname == nickname), None)
        if existing_user:
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        found = next((video for video in self.videos if video.title == title), None)
        if found == None:
            return
        if self.current_user.age < 18:
            print(f"Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for i in range(found.duration):
            time.sleep(1)
            print(i + 1)
        print("Конец видео")


# Тесты:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_пупкин', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_пупкин', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
