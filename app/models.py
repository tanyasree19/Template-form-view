from django.db import models

# Create your models here.
class School(models.Model):
    School_name=models.CharField(max_length=100)
    School_location=models.CharField(max_length=100)
    School_principal=models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

