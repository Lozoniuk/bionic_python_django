from django.http import HttpResponse
from models import Student


def students_view(request):
    students = Student.objects.all()
    html = ""
    for student in students:
        html += "<p><h3>%s</h3>Id: %i, Group: %s</p>" % (student.name, student.id, student.group)
    return HttpResponse(html)
