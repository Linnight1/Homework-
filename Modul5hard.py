class User:
    def __init__(self, nickname,password,age):
        self.nickname = nickname
        self.password = password
        self.age = age
class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = 0


    def log_in(self,login,password):
        self.login = login
        self.password = password
        if password == users[login]:
            self.current_user = login
        else:
            print("Пользователь не найден.")

    def register(self,nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if self.nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            self.current_user = nickname
            self.age = age
        else:
            self.users[nickname] = password
            self.current_user = nickname
            self.age = age

    def add(self,*args):
        self.videos = Video.videos



    def get_videos(self,search_word):
        self.search_word = search_word

        for key in self.videos.keys():
            if self.search_word in key or self.search_word.capitalize() in key or self.search_word.lower() in key:
                print(key)
            else:
                continue


    def watch_video(self,title):

        if self.current_user == 0:
            print("Войдите в аккаунт чтобы смотреть видео")
        elif self.age > 18:
            from time import sleep
            for i in self.videos:
                if i == title:
                    for j in range(1, self.videos[i][0] + 1):
                        sleep(1)
                        print(j)
                    print("Конец видео")
        else:
            for i in self.videos:
                if i == title:
                    if self.videos[i][1] == False:
                        from time import sleep
                        for j in range(1, self.videos[i][0] + 1):
                            sleep(1)
                            print(j)
                        print("Конец видео")

                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

class Video():
    videos = {}


    def __init__(self,title, duration,time_now = 0,adult_mode = False):
        self.title = title
        self.duration = duration
        self.videos[title] = duration,adult_mode
        time_now = 0







ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()


