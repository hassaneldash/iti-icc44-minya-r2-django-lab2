from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, Student

def index(request):
    return redirect('home')

def home(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    return render(request, 'application/home.html')

def about(request):
    return render(request, 'application/About.html')

def create_student(request):
    if not request.session.get('user_email') or not request.session.get('user_password'):
        return render(request, 'application/register.html')
    return render(request, 'application/create_student.html')

def register(request):
    return render(request, 'application/register.html')

def login(request):
    return render(request, 'application/login.html')

def create_user(request):
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            uname = request.POST['uname']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create(
                fname=fname,
                lname=lname,
                uname=uname,
                email=email,
                password=password
            )
            return redirect('login') 
        else:
            return render(request, 'application/register.html')
        

# def create_user(request):
#     if request.method == 'POST':
#         user_data = request.POST
#         User.objects.create(
#             fname = user_data['fname'],
#             lname = user_data['lname'],
#             uname = user_data['uname'],
#             email = user_data['email'],
#             password = user_data['password']
#         )
#         return redirect('login')
#     else:
#         return render(request, 'application/register.html')

def accept_user(request):
    if request.method == 'POST':
        user_data = request.POST
        user = User.objects.filter(email=user_data['email'], password=user_data['password']).first()
        if user:
            request.session['user_email'] = user.email
            request.session['user_password'] = user.password
            return redirect('home')
    return render(request, 'application/register.html')


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

def logout(request):
    request.session.clear()
    return render(request, 'application/register.html')