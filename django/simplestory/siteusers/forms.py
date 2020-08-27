from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import SiteUser


from ssusers.models import Account


from django.utils import timezone
import datetime


class SiteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SiteUser
        fields = [
        'username',
        'email',
        'password1',
        'password2',
        'gender',
        'name',
        'birthday',
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SiteUserCreationForm, self).save(commit=False)
        username=self.cleaned_data['username']
        password=self.cleaned_data['password1']
        email=self.cleaned_data['email']
        gender=self.cleaned_data['gender']
        if gender == 'M':
            gender=0
        else:
            gender=1
        birthday=self.cleaned_data['birthday']
        #birthday=datetime.date(1970, 6, 4)
        ssaccount=Account(
            pin='1234',
            pic='123456',
            name=username,
            password=password,
            birthday=birthday,
            loggedin=0,
            createdat=timezone.now(),
            banned=0,
            nxcredit=10000,
            characterslots=3,
            gender=gender,
            #tempban=timezone.now(),
            greason=0,
            tos=1,
            rewardpoints=0,
            votepoints=0,
            hwid=0000-0000,
            language=2
            )
        if commit:
            user.save()
            ssaccount.save()
        return user

class SiteUserChangeForm(UserChangeForm):

    class Meta:
        model = SiteUser
        fields = []

class SiteUserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password.

    copied and not used form

    """
    username = forms.CharField(max_length=16)
    password1 = forms.CharField(max_length=12，label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=12，label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = SiteUser
        fields = ('username','email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
