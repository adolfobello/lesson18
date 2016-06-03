from django import forms
from .models import SignUp
import re

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # # The re.I flag means ignore case
        # if re.search('\.edu$',email, re.I) == None:
        #     raise forms.ValidationError('Please, use a valid .EDU college email address')

        # La forma anterior es mas precisa para USA colleges. La siguiente no toma en cuenta
        # que pueden existir corros con la forma: abc@staff.acollege.edu
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if 'edu' != extension:
            raise forms.ValidationError('Please, use a valid .EDU college email address')
        return email
