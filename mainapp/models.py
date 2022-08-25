from django.db import models
from enroll.models import *

# Create your models here.

class CertificateLevel(models.Model):
    Level = models.CharField(max_length=10)
    def __str__(self):
        return self.Level

class CertificateName(models.Model):
    LevelCertificate = models.ForeignKey(CertificateLevel, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

class Usercertificate(models.Model):
    author = models.ForeignKey('enroll.User', related_name = 'user', on_delete=models.CASCADE, default='')
    certificate = models.ForeignKey(CertificateName, related_name = 'certificatetype', on_delete=models.CASCADE)
    filepath = models.FileField()
    date = models.DateTimeField(auto_now=True)

class JobType(models.Model):
    name = models.CharField(max_length=256)