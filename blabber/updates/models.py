from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Status(models.Model):
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)

class Favorites(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
