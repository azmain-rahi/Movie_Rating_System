from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from .validators import ASCIIUsernameValidator

class CustomUser(AbstractUser):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.username