from django import forms

from django.contrib.auth import get_user_model

Author = get_user_model()

class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            self.add_error("password","password must be equal")
        return cleaned_data

    class Meta:
        model = Author
        fields = ("email","username","password","password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())