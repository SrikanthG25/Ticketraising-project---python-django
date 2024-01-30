from django.db import models


class admin(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 20)
    email = models.EmailField()
