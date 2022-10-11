from django.shortcuts import render
from mainapp.models import *
from mainapp.serializers import *
from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from mainapp.permissions import IsOwner
from mainapp.permissions import IsOwner

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
        queryset = job.objects.filter(author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class JobAssignmentEmployer(APIView):
    serializer_class = JobAssignmentSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = [JWTAuthentication]


    def post(self, request, pk):
        data = request.data
        print(pk)
        print(data)
        job_assignment_obj=jobassignment.objects.filter(job_id=pk,assigned_to=data['assigned_to'],owner=self.request.user)
        if job_assignment_obj.exists():
            job_assignment_obj=jobassignment.objects.get(job_id=pk,assigned_to=data['assigned_to'],owner=self.request.user)
            job_assignment_obj.assignment_status="assigned"
            job_assignment_obj.save()
            return Response("Assigned successfully",status=status.HTTP_200_OK)
        data["job_id"] = pk
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, request, pk, format=None):
        assignments = jobassignment.objects.filter(job_id=pk).exclude(assignment_status="unassigned")
        serializer = self.serializer_class(assignments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class JobAssignmentUnassignEmployee(APIView):
    serializer_class = JobAssignmentSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    authentication_classes = [JWTAuthentication]
    def put(self, request, job_id, assignment_id, format=None):
        try:
            assignment = jobassignment.objects.get(id=assignment_id)
            serializer = self.serializer_class(assignment, data={'assignment_status': request.data.get('assignment_status')}, partial=True)
            if serializer.is_valid():
                serializer.save()
                serialized_data = serializer.data
                return Response(serialized_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except jobassignment.DoesNotExist:
            return Response({'error': "assignment does not exist"}, status=status.HTTP_400_BAD_REQUEST)

class JobAssignmentListEmployee(generics.ListAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, IsOwner,)
    

    def get(self, request, format=None):
        assignments = jobassignment.objects.filter(assigned_to=request.user.id).exclude(assignment_status="unassigned")
        serializer = JobAssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



















