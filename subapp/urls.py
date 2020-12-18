"""subapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from phonebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phonebook/index/<int:pageNum>/', views.index,name ='index'),
    path('phonebook/add', views.add, name ='add'),
    path('phonebook/detail/<int:userID>/', views.detail, name ='detail'),
    path('phonebook/update/<int:userID>/', views.update, name ='update'),
    path('phonebook/delete/<int:userID>/', views.delete, name ='delete'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register', views.createAccount, name='createAccount'),
    path('mainIndex/', views.mainIndex, name='mainIndex'),
    path('', views.index2,name='in'),
    path('page/<int:num>/', views.page, name="page")
]
