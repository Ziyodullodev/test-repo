import uuid
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    telegram_id = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    language = models.CharField(max_length=2, default='uz')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }

    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def check_empty_password(self):
        if not self.username:
            username = f'username-{uuid.uuid4().__str__().split("-")[-1]}'
            
        if not self.password:
            password = f'password-{uuid.uuid4().__str__().split("-")[-1]}'
            self.password = password


    def save(self, *args, **kwargs):
        self.check_empty_password()
        self.check_hash_password()
        super(User, self).save(*args, **kwargs)

