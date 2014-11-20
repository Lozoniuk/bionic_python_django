from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return self.name


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
