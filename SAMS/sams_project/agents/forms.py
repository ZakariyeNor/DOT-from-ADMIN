from django import forms
from .models import Mission, Agent, MissionLog

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['name', 'description', 'mission_type', 'status', 'start_date', 'end_date', 'agents']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'agents': forms.CheckboxSelectMultiple(),
        }

class MissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['status', 'progress_percentage']

class MissionLogForm(forms.ModelForm):
    class Meta:
        model = MissionLog
        fields = ['note', 'agent']
