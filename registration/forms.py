from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'university']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={}),
            'bio': forms.Textarea(attrs={}),
            'link': forms.URLInput(attrs={}),
            'university': forms.Textarea(),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=254,
                             help_text="Required. 254 characters at maximum end must be a valid email")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(u'THe email is registered, try other.')
            return email
