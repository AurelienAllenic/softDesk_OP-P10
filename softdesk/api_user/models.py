from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    age = models.PositiveIntegerField(_('age'), default=0)
    consent = models.BooleanField(default=False)
    
    def clean(self):
        if self.is_superuser:
            self.age = None
        super().clean()
        if self.age is not None and self.age < 15:
            raise ValidationError(_('You must be at least 15 years old to register.'))

    def save(self, *args, **kwargs):
        if self.age is None:
            raise ValidationError(_('Age field cannot be null.'))
        if self.email == '':
            raise ValidationError(_('Email field cannot be null.'))
        super().save(*args, **kwargs)
