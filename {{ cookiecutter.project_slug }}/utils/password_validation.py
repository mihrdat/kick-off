from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class SpecialCharPasswordValidator:
    """
    Validates that the password contain at least 1 special character.
    """

    def validate(self, password, user=None):
        chars = "[@_!#$%^&*()<>?/\|}{~:]"

        if not re.findall(chars, password):
            raise ValidationError(
                _(f"This password doesn't contain any special characters: {chars}."),
                code="password_no_symbol",
            )


class UppercasePasswordValidator:
    """
    Validates that the password contain at least 1 uppercase letter, A-Z.
    """

    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                _("This password doesn't contain uppercase letter, A-Z."),
                code="password_no_upper",
            )
