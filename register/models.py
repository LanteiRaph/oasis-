import email
from django.db import models

# Create your models here.
from typing import Reversible
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone



class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/register/users/%i/" % (self.pk)


class Profile(models.Model):
  user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  name= models.TextField(max_length=255)
  is_student = models.BooleanField(blank=True, null=True)
  student_id = models.TextField(max_length=30, blank=True, null=True)
  course_name = models.TextField(max_length=255, blank=True, null=True)
  phone = models.TextField(max_length=100)


  def __str__(self) -> str:
        return self.name

  def get_absolute_url(self):
        return "/register/users/%i/" % (self.pk)