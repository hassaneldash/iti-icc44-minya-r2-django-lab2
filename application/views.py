from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Student
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User as django_user

def index(request):
    return redirect('home')

def home(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    return render(request, 'application/home.html')

def about(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    return render(request, 'application/About.html')

def create_student(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    return render(request, 'application/create_student.html')

def register(request):
    return render(request, 'application/register.html')

def login(request):
    return render(request, 'application/login.html')

# # ______________ Lab No.03 (Working✔️) ______________
# def createusers(request):
#     if request.method == 'POST':
#         first_name = request.POST['fname']
#         last_name = request.POST['lname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             password=password
#         )
#         user.save()
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('home')  
#         else:
#             return redirect('register')
#     else:
#         return render(request, 'application/register.html')


# ______________ Lab No.02 (Working✔️) ______________
def createusers(request):
    if request.method == 'POST':
        user_data = request.POST
        User.objects.create(
            fname = user_data['fname'],
            lname = user_data['lname'],
            username = user_data['username'],
            email = user_data['email'],
            password = user_data['password']
        )
        return redirect('login')
    else:
        return render(request, 'application/register.html')



# # ______________ Lab No.03 ______________
# def createusers(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already exists.')
#             return render(request, 'application/register.html')
        
#         django_user.objects.create_user(
#             username = username,
#             email = email,
#             password = password
#         )
#         return redirect('login')
#     else:
#         return render(request, 'application/register.html')


# ______________ Lab No.02 (Working✔️) ______________
def accept_user(request):
    if request.method == 'POST':
        user_data = request.POST
        user = User.objects.filter(email=user_data['email'], password=user_data['password']).first()
        if user:
            request.session['user_email'] = user.email
            request.session['user_password'] = user.password
            return redirect('home')
    return render(request, 'application/register.html')


# # ______________ Lab No.03 (Working✔️) ______________
# def accept_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         myuser = User.objects.filter(email=email).first()
#         if myuser:
#             auth = authenticate(request, username=myuser[0].username, password=password)
#             print(auth)
#             if auth is not None:
#                 django_login(request, auth)
#                 return redirect('home')
#         else:
#             return render(request, 'application/login.html')
#     else:
#         return render(request, 'application/login.html')
#     return render(request, 'application/register.html')

def create_student(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        messages.error(request, 'You need to be logged in to access this page.')
        return render(request, 'application/register.html')
    
    if request.method == 'POST':
        student_data = request.POST
        Student.objects.create(
            s_name=student_data['fname'],
            age=student_data['age'],
            s_email=student_data['email']
        )
        return redirect('show_user')
    else:
        return render(request, 'application/create_student.html')


def show_user(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    students = Student.objects.all()
    return render(request, 'application/show_user.html', {'students': students})

def delete_student(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return redirect('show_user')

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student_data = request.POST
        student.s_name = student_data['fname']
        student.s_email = student_data['email']
        student.age = student_data['age']
        student.save()
        return redirect('show_user')
    return render(request, 'application/edit_student.html', {'student': student})

## ______________ Lab No.02 (Working✔️) ______________
# def logout(request):
#     request.session.clear()
#     return render(request, 'application/register.html')


# ______________ Lab No.03 (Working✔️) ______________
def logout(request):
    django_logout(request)
    return render(request, 'application/register.html')