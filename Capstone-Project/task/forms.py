from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    service_no = forms.CharField(max_length=15)
    rank = forms.CharField(options=['ACM','LCPL','CPL','SGT',
                                    'FS','WO','MWO','AWO','PLT OFFR',
                                    'FG OFFR','FLT LT','SQN LDR','WG CDR',
                                    'GP CAPT','AIR CDR','AVM'])
    email = forms.EmailField()

    class Meta:
        form = UserCreationForm
        fields = ('__all__')
    
    def clean(self):
        cleaned = super().clean()
        return cleaned
        