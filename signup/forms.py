from django import forms
from .models import Signup

# This is to capture email and save it in teh backend

class SignupModelForm(forms.ModelForm):
    name       = forms.CharField(widget=forms.TextInput(
                        attrs={
                            'placeholder':'Your name:',
                            'class':'form-control',
                        }
                    ))
    email       = forms.EmailField(label='',
                    widget=forms.EmailInput(
                        attrs={
                            'placeholder':'Your email:',
                            'class':'form-control'
                        }
                    ))

    class Meta:
        model = Signup
        fields = [
            'name',
            'email'
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        qs = Signup.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Sorry buddy, this email exists")
        return email