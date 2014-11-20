from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'coursera.views.main'),
    url(r'^register/', 'coursera.views.add_student_view'),
    url(r'^register.do/', 'coursera.views.add_student_action'),
    url(r'^login.do/', 'coursera.views.login_student_action'),
    url(r'^students/', 'coursera.views.students_view'),
    url(r'^admin/', include(admin.site.urls)),
)
