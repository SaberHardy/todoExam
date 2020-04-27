from django import forms
from .models import ToDo

class ListForm(forms.ModelForm):
	class Meta:
		model = ToDo
		fields = ['content','completed']

  