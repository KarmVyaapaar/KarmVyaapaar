"""KarmVyaapaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('employerprofile',views.employ,name="employer"),
    path('worker',views.worker,name="worker"),
    path('history',views.history,name="history"),
    path('notification',views.notify,name="notification"),
    path('FAQs',views.FAQ,name="FAQs"),
    path('logout',views.logoutuser,name="signout"),
    path('loginWorker',views.loginWorker,name="loginWorker"),
    path('search',views.search,name='search'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
