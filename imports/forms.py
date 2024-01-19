from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import JobApplication



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',  
            'password2',
        ]
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = _('Username')
        self.fields['first_name'].widget.attrs['placeholder'] = _('First Name')
        self.fields['last_name'].widget.attrs['placeholder'] = _('Last Name')
        self.fields['email'].widget.attrs['placeholder'] = _('Email')
        self.fields['password1'].widget.attrs['placeholder'] = _('Password')
        self.fields['password2'].widget.attrs['placeholder'] = _('Confirm Password')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
    


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'name',
            'email',
            'whatsapp_number',
            'country',
            'city',
            'cv',
        ]
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'whatsapp_number': _('WhatsApp Number'),
            'country': _('Country'),
            'city': _('City'),
            'cv': _('Curriculum Vitae'),
        }

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        # Set the cv field as optional
        self.fields['cv'].required = False