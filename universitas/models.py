from django.db import models

# Create your models here.
class Fakultas(models.Model):
    no = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    

    def __str__(self):
        return self.no