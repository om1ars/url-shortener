from django.db import models

class Url(models.Model):
    link = models.CharField()