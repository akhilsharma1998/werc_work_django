from django.shortcuts import render
from mainapp.models import *
from mainapp.serializers import *
from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# With the help of this API we can get full list of certificates level.

class CreateCertificateLevel(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = CertificateLevel.objects.all()
    serializer_class = CertificateLevelSerializer

# With the help of this API we can get list of all certificates name with level.
# We can also create certificate with the help of this API.

class CreateCertificateName(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = CertificateName.objects.all()
    serializer_class = CertificateNameSerializer

# With the help of this api user can get all list of their certificates and upload certificate as well.

class UsercertificateUpload(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Usercertificate.objects.all()
    serializer_class = UsercertificateSerializer

    def get_queryset(self):
        queryset = Usercertificate.objects.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# user can get their single uploaded certificate

class UsercertificateDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = Usercertificate.objects.all()
    serializer_class = UsercertificateSerializer

    def get_queryset(self):
        queryset = Usercertificate.objects.filter(author=self.request.user)
        return queryset

# with the help of this api user can get all jobtype.

class JobTypeList(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

# with the help of this api we can create and get  job.

class JobListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Usercertificate.objects.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


















