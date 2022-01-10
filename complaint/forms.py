from django import forms
from .models import Complaint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterComplaintForm(forms.ModelForm):
    photo = forms.ImageField(allow_empty_file=True,
                             required=False,)
    class Meta:
        model = Complaint
        fields = ('title', 'description', 'category', 'photo')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']