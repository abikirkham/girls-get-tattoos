from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            
            if hasattr(self.instance, 'get_friendly_name'):
                friendly_name = getattr(self.instance, 'get_friendly_name', None)
                if friendly_name:
                    field.label = friendly_name() 
