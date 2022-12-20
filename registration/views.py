from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWIthEmail
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = "registration/profile_form.html"


class SignUpView(CreateView):
    form_class = UserCreationFormWIthEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', 'placeholder': 'Name'})
        form.fields['email'].widget = forms.EmailInput( attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', 'placeholder': 'Password'})
        form.fields['password2'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', 'placeholder': 'Repeat Password'})
        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        return form
