

import re
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+\-\s]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, spaces, and @/./+/-/_ characters.'
    )
    flags = 0

class AllowSimplePasswordValidator:
    """
    This validator allows simple passwords like "pass1".
    """

    def validate(self, password, user=None):
        # No validation check for this validator
        pass

    def get_help_text(self):
        return _("Your password can be a simple string like 'pass1'.")


