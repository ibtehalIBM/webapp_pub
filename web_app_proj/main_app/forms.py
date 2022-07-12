from datetime import date

from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

