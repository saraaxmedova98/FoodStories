from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    username = models.CharField(_("Username"), max_length=50 , blank=True)
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(_("Biography"), blank=True, null=True)
    profile_image = models.ImageField(_("Image"), upload_to='authors/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




