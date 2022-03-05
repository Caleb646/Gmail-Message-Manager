from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from . import models as m


class MyUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = m.MyUser
        fields = ('email', 'user_type', 'groups',)


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = m.MyUser
        fields = ('email', 'user_type', 'groups',)


class DashboardCreateForm(forms.ModelForm):
    class Meta: 
       model = m.Dashboard
       fields = ['owner']

class DashboardChangeForm(forms.ModelForm):
    class Meta: 
       model = m.Dashboard
       fields = ['owner']

class MessageThreadUpdateForm(forms.Form):
    job_id = forms.CharField()
    pub_date = forms.DateField()