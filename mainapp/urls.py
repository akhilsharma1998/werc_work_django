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
    path('SingleJobListCreate/<int:pk>/', SingleJobListCreate.as_view(), name='SingleJobListCreate'),
]