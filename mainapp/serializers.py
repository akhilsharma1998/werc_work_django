from rest_framework import serializers
from mainapp.models import *
from enroll.models import *

class CertificateLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateLevel
        fields=(
            'id',
            'Level'
        )

class CertificateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateName
        fields=(
            'id',
            'LevelCertificate',
            'title'
        )

class UsercertificateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Usercertificate
        fields = (
            'id',
            'author',
            'certificate',
            'filepath',
            'date'
        )

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = (
            'id',
            'name'
        )

class JobSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = job
        fields = (
            'id',
            'author',
            'typejob',
            'description',
            'date'
        )

class JobassignmentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = job_assignment
        fields = (
            'id',
            'author',
            'assigned_to',
            'job_id',
            'assign_time',
            'assignment_status'
        )

class JobassignmentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = job_assignment
        fields = (
            'id',
            'author',
            'assigned_to',
            'job_id',
            'assign_time',
            'assignment_status'
        )


