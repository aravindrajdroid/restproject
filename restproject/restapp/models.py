from django.db import models

class UserModel(models.Model):
    programming_lang = models.CharField(max_length=30)
    