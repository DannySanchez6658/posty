from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)

class Post(models.Model):
    user = models.ForeignKey(User)
    post = models.TextField()