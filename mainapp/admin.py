from django.contrib import admin
from mainapp.models import CertificateLevel, CertificateName, Usercertificate, JobType, job, job_assignment

# Register your models here.

admin.site.register(CertificateLevel)
admin.site.register(CertificateName)
admin.site.register(Usercertificate)
admin.site.register(JobType)
admin.site.register(job)
admin.site.register(job_assignment)