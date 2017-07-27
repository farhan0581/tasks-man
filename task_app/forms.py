from django import forms
from django.contrib.auth.models import User
from task_app.models import Tasks

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def authenticate_using_email(self):
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                pass
        return None

    class Meta:
        model = User
        fields = ['email', 'password']


class DateInput(forms.DateInput):
    input_type = 'date'

class TaskAddForm(forms.ModelForm):
    name = forms.CharField()
    deadline = forms.DateField(label='deadline', input_formats=['%Y-%m-%d'],
                                widget=DateInput()
                              )
    complete_by = forms.DateField(label='complete by', required=False, input_formats=['%Y-%m-%d'],
                                widget=DateInput() 
                              )
    class Meta:
        model = Tasks
        fields = ['name', 'deadline', 'complete_by']