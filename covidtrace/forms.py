from django.forms import ModelForm
from .models import Barangay, Citymun

class BarangayForm (ModelForm):
    class Meta:
        model = Barangay
        fields = '__all__'


class CitymunForm (ModelForm):
    class Meta:
        model = Citymun
        fields = '__all__'
