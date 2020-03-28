from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    platform = models.CharField(max_length=50, choices=(
        ('web', 'Web'),
        ('mobile', 'Mobile'),
        ('tablet', 'Tablet'),
    ))
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name
