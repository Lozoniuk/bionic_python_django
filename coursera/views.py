from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from models import Student
from django.contrib.auth import authenticate, login


def main(request):
    return render_to_response("coursera/main.html", {'user': request.user})


def add_student_view(request):
    return render_to_response('coursera/register.html')


def add_student_action(request):
    username = request.REQUEST['username']
    password = request.REQUEST['password']

    exist_student_list = Student.objects.filter(username=username)
    if len(exist_student_list) == 0:
        new_student = Student(username=username)
        new_student.set_password(password)
        new_student.save()
        new_student = authenticate(username=username, password=password)
        login(request, new_student)
        return redirect('/')
    else:
        return render_to_response('coursera/main.html', {'error': 'The username already exists'})


def login_student_action(request):
    username = request.REQUEST['username']
    password = request.REQUEST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return render_to_response('coursera/main.html', {'error': 'disabled account'})
    else:
        return render_to_response('coursera/main.html', {'error': 'invalid login'})


def students_view(request):
    students = Student.objects.all()
    html = ""
    for student in students:
        html += "<p><h3>%s</h3>Id: %i, Group: %s</p>" % (student.username, student.id, student.group)
    return HttpResponse(html)
