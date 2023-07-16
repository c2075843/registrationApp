
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,Group
from accounts.models import Student


class Module(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    credit=models.IntegerField()
    description=models.TextField()
    category=models.CharField(max_length=100)
    availability=models.BooleanField(default=True)
    courses=models.ManyToManyField(Group, related_name="modules") 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('courseapp:module-list', kwargs = {'pk': self.pk})
    


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student ID: {self.student.user.username} registered for: {self.module.name}"

    