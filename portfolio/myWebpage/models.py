from django.db import models
import datetime as dt
# Create your models here.
class feedback(models.Model):
    email = models.EmailField("email", max_length=54)
    feed = models.TextField("feedback",max_length=250)
    date = models.DateField("date", auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.email