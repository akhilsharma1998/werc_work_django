from django.contrib import admin
from django.urls import path, include
from mainapp.views import *

urlpatterns = [
    path('CreateCertificateLevel/', CreateCertificateLevel.as_view(), name='CreateCertificateLevel'),
    path('CreateCertificateName/', CreateCertificateName.as_view(), name='CreateCertificateName'),
    path('UsercertificateUpload/', UsercertificateUpload.as_view(), name='UsercertificateUpload'),
    path('UsercertificateDetail/<int:pk>/', UsercertificateDetail.as_view(), name='UsercertificateDetail'),
    path('JobTypeList/', JobTypeList.as_view(), name='JobTypeList'),
    path('JobListCreate/', JobListCreate.as_view(), name='JobListCreate'),
    path('SingleJob/<int:pk>/', SingleJob.as_view(), name='SingleJob'),
    path('updateSingleJob/<int:pk>/', SingleJob.as_view(), name='updateSingleJob'),
    path('deleteSingleJob/<int:pk>/', SingleJob.as_view(), name='updateSingleJob'),

    path('jobs/assignments/<int:pk>/notes/', NotesEmployee.as_view(), name='notes'),
]