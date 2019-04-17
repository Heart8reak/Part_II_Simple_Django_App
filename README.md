## Part II
## Continue with the backend of the web app
## Add email validation and confirmation

1.0 Sync the database
```bash
python manage.py makemigrations
python manage.py migrate
```

1.0.1 Create Super User
```bash
python manage.py createsuperuser
```

1.1 Create a database with PostGres, in the terminal launch postgres
```bash
psql
```
1.1.1 List out all databases
```bash
\l
```
1.1.2 If you need to delete a database
```bash
DROP DATABASE meetupnews001;
```
1.1.3 Create a new database:
```bash
CREATE DATABASE meetupnews002;

CREATE USER admin003 WITH PASSWORD 'admin002';

ALTER ROLE admin003 SET client_encoding TO 'utf8';

ALTER ROLE admin003 SET default_transaction_isolation TO 'read committed';

ALTER ROLE admin003 SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE meetupnews002 TO admin003;
```
1.2 Add Postgres Database to settings.py file
```python
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meetupnews002',
        'USER': 'admin003',
        'PASSWORD': 'admin002',
        'HOST': 'localhost',
        'PORT': '5432',
        }
    }
```

1.3 Now we need to sync the database with making migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

1.3.1 We need to recreate a new superuser, becuase we are using a new database
```bash
python manage.py createsuperuser
```

2.0 Go to models.py and create the model for the backend
```python
class Signup(models.Model):
    name        = models.CharField(max_length=120)
    email       = models.EmaiField(blank=False, null=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
```

2.0.1 sync the database
```bash
python manage.py makemigrations
python migrate
```

2.1 Goto admin.py and register the new models
```python
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_filter     = ['name','email','timestamp']
    list_display    = ['name','email','timestamp']

admin.site.register(Signup,SignupAdmin)
```

2.2 Create a forms.py file in the app directory, we are adding a validation function for emails
```python
from django import forms
from .models import Signup

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
```

2.3 Go to views.py file and update the signup function to reflect the forms.py
```python
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SignupModelForm

def signup_view(request):
    form = SignupModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Thanks for signing up!")
        return redirect('/')
    context = {"form":form}
    return render(request, "signup.html", context)
```

2.4 Go to the Heroku dashboar

2.5 click on Heroku Postgres configure Add-ons

2.5.1 click on settings

2.5.2 click on view credentials

2.6 copy the credentials into the settings.py

3.0 Update Github and push to heroku live
```bash
git status
git add .
git commit -m "Created the backend"
git push heroku master
```

3.1. In the terminal create the super user for the backend
```bash
heroku run python manage.py createsuperuser
```


## Web App
https://meetup003.herokuapp.com/
