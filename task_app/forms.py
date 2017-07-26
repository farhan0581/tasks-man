from django import forms
from task_app.models import UserProfile

class UserProfileForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = UserProfile
		fields = '__all__'