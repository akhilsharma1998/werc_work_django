from django.db import models
from enroll.managers import CustomUserManager
from pyexpat import model
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    EMPLOYER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (EMPLOYER, 'Employer'),
        (EMPLOYEE, 'Employee')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    dob = models.DateTimeField(blank=True, null=True)             
    mobile_number = models.CharField(max_length=12, default='')
    allergies = models.TextField(max_length=250, default='')
    medical_issues = models.TextField(max_length=250, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
