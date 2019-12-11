from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    testimoni = models.CharField(max_length=200)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.nama

class Mentee(models.Model):
    nama = models.CharField(max_length=100)
    testimoni = models.CharField(max_length=200)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.nama

class Blog(models.Model):
    judul = models.CharField(max_length=1000)
    artikel = models.CharField(max_length=10000)
    picture = models.CharField(max_length=1000)
    tanggal = models.DateField()

    def __str__(self):
        return self.judul


