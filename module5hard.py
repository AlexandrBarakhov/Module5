"""

Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же следует учитывать следущие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"

Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')

Вывод в консоль:
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist

Примечания:
Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др.
Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные вариации.

"""


from time import sleep
from hashlib import sha256


def hash_password(password: str) -> int:
    """Хеширует пароль с помощью SHA256"""
    return int(sha256(password.encode('utf-8')).hexdigest(), 16)


class User:
    """Класс для представления пользователя"""

    def __init__(self, nickname: str, password: str, age: int):
        """Инициализирует объект User"""
        self.nickname = nickname
        self.password = hash_password(password)
        self.age = age

    def __str__(self) -> str:
        """Возвращает строковое представление объекта User"""
        return self.nickname

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта User для отладки"""
        return f"User(nickname='{self.nickname}', age={self.age})"


class Video:
    """Класс для представления видео"""

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        """Инициализирует объект Video"""
        self.title = title.capitalize()  # Добавленное видео будет с заглавной буквы
        self.duration = duration
        self.time_now = 0  # Инициализируем time_now здесь
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Video"""
        return f"Видео: '{self.title}', длительность: {self.duration} секунд"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Video для отладки"""
        return (
            f"Video(title='{self.title}', duration={self.duration}, "
            f"adult_mode={self.adult_mode})"
        )

    def __eq__(self, other) -> bool:
        """Сравнивает два объекта Video по названию"""
        if isinstance(other, Video):
            return self.title == other.title
        return False

    def __contains__(self, item: str) -> bool:
        """Проверяет, содержится ли подстрока item в названии видео"""
        return item.lower() in self.title.lower()


class UrTube:
    """Класс для представления платформы UrTube"""

    def __init__(self):
        """Инициализирует объект UrTube"""
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user: User | None = None

    def log_in(self, nickname: str, password: str) -> None:
        """Выполняет вход пользователя"""
        password_hash = hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Вход выполнен. Здравствуйте, {user.nickname}!")
                return
        print("Неверное имя пользователя или пароль")

    def register(self, nickname: str, password: str, age: int) -> None:
        """Регистрирует нового пользователя"""
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        # print(f"Регистрация прошла успешно. Здравствуйте, {nickname}!")

    def log_out(self) -> None:
        """Завершает сеанс текущего пользователя"""
        self.current_user = None
        print("Выход из аккаунта выполнен")

    def add(self, *new_videos: Video) -> None:
        """Добавляет новые видео, если их еще нет"""
        for video in new_videos:
            if video not in self.videos:
                self.videos.append(video)
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search: str) -> list[str]:
        """Возвращает список названий видео, содержащих поисковый запрос"""
        return [
            video.title
            for video in self.videos
            if search.lower() in video.title.lower()  # можно просто if search in video
        ]                                             # т.к. есть __contains__ в классе Video, но это не точно

    def watch_video(self, video_title: str) -> None:
        """Воспроизводит видео, если оно найдено и доступно"""
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return

                video.time_now = 0
                # print(f"Воспроизведение видео: {video.title}")
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=' ')
                    sleep(1)
                print("Конец видео")
                return

        # print(f"Видео с названием '{video_title}' не найдено")


if __name__ == '__main__':
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
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
