from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'industry': forms.TextInput(attrs={'placeholder': 'Comma-separated values (e.g., tech, finance, healthcare)'}),
            'company_culture': forms.TextInput(attrs={'placeholder': 'Comma-separated values'}),
            'core_values': forms.TextInput(attrs={'placeholder': 'Comma-separated values'}),
            'skills_required': forms.TextInput(attrs={'placeholder': 'Comma-separated values (e.g., python, javascript, leadership)'}),
            'languages_required': forms.TextInput(attrs={'placeholder': 'Comma-separated values (e.g., English, French, Spanish)'}),
            'personality_required': forms.TextInput(attrs={'placeholder': 'Comma-separated values (e.g., creative, analytical, team-player)'}),
            'benefits_offered': forms.TextInput(attrs={'placeholder': 'Comma-separated values'}),
            'name': forms.TextInput(attrs={'placeholder': 'Company name'}),
            'size': forms.TextInput(attrs={'placeholder': 'e.g., 10-50, 50-200, 200+'}),
            'location_pref': forms.TextInput(attrs={'placeholder': 'e.g., Remote, On-site, Hybrid'}),
            'work_pace': forms.TextInput(attrs={'placeholder': 'e.g., Fast-paced, Moderate, Slow'}),
            'management_style': forms.TextInput(attrs={'placeholder': 'e.g., Democratic, Autocratic, Laissez-faire'}),
            'work_life_balance': forms.TextInput(attrs={'placeholder': 'e.g., Excellent, Good, Poor'}),
            'experience_level_required': forms.TextInput(attrs={'placeholder': 'e.g., Junior, Mid, Senior'}),
            'risk_tolerance': forms.TextInput(attrs={'placeholder': 'e.g., High, Medium, Low'}),
            'salary_range': forms.TextInput(attrs={'placeholder': 'e.g., $50k-$80k'}),
        }
