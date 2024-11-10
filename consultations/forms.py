from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        friendly_names = [(c.id, c.get_friendly_name())]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'