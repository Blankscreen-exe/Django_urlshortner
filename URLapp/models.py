from django.db import models

class URL(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)
