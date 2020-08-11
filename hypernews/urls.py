"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from news.views import main, news, all_news, post, about, login, signup, profile, logout, change_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('news/<int:news_number>/', news),
    path('news/', all_news),
    path('news/create/', post),
    path('about/', about),
    path('login', login),
    path('signup', signup),
    path('profile', profile),
    path('logout', logout),
    path('change/password/', change_password)
]
urlpatterns += static(settings.STATIC_URL)
