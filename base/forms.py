from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    # lastname = forms.CharField(max_length=100)  # Add lastname field to the form

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include lastname field in fields list

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.last_name = self.cleaned_data['lastname']  # Save lastname field to user's last_name attribute
    #     if commit:
    #         user.save()
    #     return user
