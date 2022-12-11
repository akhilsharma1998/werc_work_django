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

class notes(models.Model):
    job_assignment_id = models.ForeignKey(jobassignment, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(jobs, on_delete=models.CASCADE, blank=True, null=True)

class workinghourr(models.Model):
    Status = (
        ('in_progress', 'in_progress'),
        ('pause', 'pause'),
        ('ended', 'ended'),
    )
    author = models.ForeignKey('enroll.User', related_name = 'userr', on_delete=models.CASCADE)
    job_assignment_id = models.ForeignKey(jobassignment, related_name='jbassign', on_delete=models.CASCADE)
    logging_hour_start = models.DateTimeField(null=True, blank=True)
    logging_hour_end = models.DateTimeField(null=True, blank=True)
    log_status = models.CharField(max_length=250, choices=Status, default='in_progress')

class FAQ(models.Model):
    question = models.CharField(max_length=1024)
    answer = models.TextField()
    active = models.BooleanField(default=True, help_text='Whether to show this question or not')

