from django.db import models

class Project(models.Model):
    started = models.DateTimeField()
    finished = models.DateTimeField()
    title = models.CharField(max_length=100, blank=True, default='')
    short_description = models.CharField(max_length=250, blank=True, default='')
    descriptions = models.TextField()
    url = models.CharField(max_length=100, blank=True, default='')
    github = models.CharField(max_length=200, blank=True, default='')
    video = models.CharField(max_length=200, blank=True, default='')