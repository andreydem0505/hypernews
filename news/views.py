from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User, News
from .forms import UserForm


user = None


def main(request):
    global user
    return render(request, 'news/main.html', {"user": user})


def news(request, news_number):
    global user
    dic = News.objects.all()
    for el in dic:
        if el.link == news_number:
            total = el
    return render(request, "news/news.html", {"post": total, "user": user})


def all_news(request):
    global user
    error = ''
    dic = News.objects.all()
    for el in dic:
        el.link = str(el.link)
        el.created = el.created[:10]
    bigdict = {}

    q = request.GET.get("q")
    if q:
        for el in dic:
            if q in el.title:
                if el.created not in bigdict:
                    bigdict[el.created] = [el]
                else:
                    bigdict[el.created].append(el)
        if len(bigdict) == 0:
            error = 'По Вашему запросу ничего не найдено'
    else:
        for el in dic:
            if el.permission:
                if el.created not in bigdict:
                    bigdict[el.created] = [el]
                else:
                    bigdict[el.created].append(el)
    list_keys = list(bigdict.keys())
    list_keys.sort(reverse=True)
    bigdict2 = {}
    for i in list_keys:
        bigdict2[i] = bigdict[i]
    return render(request, "news/all_news.html", {"news": bigdict2, 'error': error, "user": user})


def post(request):
    global user
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        News.objects.create(author=user, text=text, title=title)
        return redirect("/news/")
    return render(request, 'news/create.html', {"user": user})


def about(request):
    global user
    return render(request, 'news/about.html', {"user": user})


def login(request):
    global user
    global theme
    error = ''
    users = User.objects.all()
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        for el in users:
            if el.login == login and el.password == password:
                user = el
                return redirect("/news")
            else:
                error = "Пароль или логин введён не верно!"

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/login.html', context)


def signup(request):
    global user
    error = ''
    users = User.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            maybe_user = request.POST.get("login")
            maybe_password = request.POST.get("password")
            if len(maybe_user) > 4:
                if len(maybe_password) > 7:
                    is_exist = False
                    for el in users:
                        if el.login == maybe_user:
                            is_exist = True
                    if is_exist == True:
                        error = 'Пользователь с таким логином уже существует'
                    else:
                        user = el
                        form.save()
                        return redirect('/news')
                else:
                    error = 'Длинна пароля должна быть больше 7 символов'
            else:
                error = 'Длинна логина должна быть больше 4 символов'
        else:
            error = 'Форма заполнена не верно'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/signup.html', context)


def profile(request):
    global user
    if user is not None:
        error = ''
        if request.method == 'POST':
            choosen = request.POST.get("theme")
            for el in User.objects.all():
                if el.login == user.login:
                    el.theme = choosen
                    el.save()
                    user = el
                    return redirect("/profile")

        dic = News.objects.all()
        for el in dic:
            el.link = str(el.link)
            el.created = el.created[:10]
        bigdict = {}
        for el in dic:
            if el.permission:
                if user.theme in el.theme:
                    if el.created not in bigdict:
                        bigdict[el.created] = [el]
                    else:
                        bigdict[el.created].append(el)
        if len(bigdict) > 0:
            list_keys = list(bigdict.keys())[:7]
            list_keys.sort(reverse=True)
            bigdict2 = {}
            for i in list_keys:
                bigdict2[i] = bigdict[i]
        else:
            error = 'На Вашу тему пока нет новостей'
            bigdict2 = ''
        return render(request, 'news/profile.html', {"user": user, "news": bigdict2, "error": error})
    else:
        return HttpResponse("<h1>:( Войдите в аккаунт, чтобы посмотреть эту страницу</h1>")


def logout(request):
    global user
    user = ''
    return redirect('/news')


def change_password(request):
    global user
    error = ''
    if user is not None:
        if request.method == 'POST':
            new_password = request.POST.get("password")
            if len(new_password) >= 8:
                for el in User.objects.all():
                    if el.login == user.login:
                        el.password = new_password
                        el.save()
                        user = el
                        return redirect("/profile")
            else:
                error = 'Длинна пароля должна быть больше 7 символов'
        return render(request, 'news/change_password.html', {"user": user, "error": error})
    else:
        return HttpResponse("<h1>:( Войдите в аккаунт, чтобы посмотреть эту страницу</h1>")