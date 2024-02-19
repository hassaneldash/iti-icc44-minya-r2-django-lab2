"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from application.views import home,about,register,login,create_user,accept_user,create_student,show_user,delete_student,edit_student,logout,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("home/",home ,name='home'),
    path("about/",about,name='about'),
    path("register/",register,name='register'),
    path("login/",login,name='login'),
    path('create_user/', create_user, name='create_user'),
    path('accept_user/', accept_user, name='accept_user'),
    path('create_student/', create_student, name='create_student'),
    path("show_users/",show_user,name='show_user'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('logout/', logout, name='logout'),
]
