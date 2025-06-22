from django import forms
from .models import ConsultationInterest


class ConsultationInterestForm(forms.ModelForm):
    class Meta:
        model = ConsultationInterest
        fields = ["topic", "preferred_date", "preferred_time", "message"]
