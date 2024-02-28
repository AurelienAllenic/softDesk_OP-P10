from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    age = models.PositiveIntegerField(_('age'), blank=True, null=True)
    
    def clean(self):
        if self.is_superuser:
            self.age = None
        super().clean()
        if self.age < 15:
            raise ValidationError(_('You must be at least 15 years old to register.'))
