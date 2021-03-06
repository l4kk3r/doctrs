from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    doctor = models.CharField(max_length=200)
    time = models.CharField(max_length=200)


    def __str__(self):
        return self.doctor + ' на ' + self.time
