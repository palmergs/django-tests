from django import forms
from .models import Goal
from .models import Prereq

class GoalForm(forms.ModelForm):

	class Meta:
		model = Goal
		fields = ('title', 'description')
		widgets = {
			'title': forms.TextInput(attrs={ 'class': 'form-control' }),
			'description': forms.Textarea(attrs={ 'class': 'form-control' })
		}

