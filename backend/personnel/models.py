from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} department"


class Personnel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    participation_date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
