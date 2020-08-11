from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    login = models.CharField("логин", max_length=20)
    password = models.CharField("пароль", max_length=20)
    email = models.CharField("почта", max_length=30, default='')
    theme = models.CharField("тема", max_length=20, default='')

    def __str__(self):
        return self.login


class News(models.Model):
    author = models.CharField("автор", max_length=20, default="admin")
    created = models.TextField("время", default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    text = models.TextField("текст", max_length=1000)
    title = models.CharField("заголовок", max_length=50)
    theme = models.CharField("тема", max_length=65, default='Политика Медицина Экономика Спорт Экология IT Авто Наука Культура')
    link = models.IntegerField("ссылка", default=0)
    permission = models.BooleanField("разрешение", default=False)

    def __str__(self):
        return f'({str(self.link)}) {self.title}'
