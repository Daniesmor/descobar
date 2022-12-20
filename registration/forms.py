from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormWIthEmail(UserCreationForm):
    email = forms.EmailField(required=True,
                             help_text="Required. 254 characters at maximum and have been a valid email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Email registered, try other.')
        return email

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
