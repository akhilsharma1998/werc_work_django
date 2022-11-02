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

class job(models.Model):
    author = models.ForeignKey('enroll.User', related_name = 'currentuser', on_delete=models.CASCADE, default='')
    typejob = models.ForeignKey(JobType, related_name = 'type', on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now=True)

class job_assignment(models.Model):
    Status = (
    ('assigned', 'assigned'),
    ('in_progress', 'in_progress'),
    ('unassigned', 'unassigned'),
    ('completed', 'completed'),
)
    author = models.ForeignKey('enroll.User', related_name = 'assign_job_author', on_delete=models.CASCADE, default='',)
    assigned_to = models.ForeignKey('enroll.User', related_name='assignperson', on_delete=models.CASCADE)
    job_id = models.ForeignKey(job, related_name='idofjob', on_delete=models.CASCADE)
    assign_time = models.DateField(auto_now=True)
    assignment_status = models.CharField(max_length=250, choices=Status, default='assigned')

# This model for notes
class notes(models.Model):
    Description = models.CharField(max_length=100)


