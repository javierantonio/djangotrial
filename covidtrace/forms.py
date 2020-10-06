from django.forms import ModelForm
from .models import Barangay, Citymun, Visitor, Establishment, Sys_user

class BarangayForm (ModelForm):
    class Meta:
        model = Barangay
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['citymun'].queryset = Citymun.objects.none()


class CitymunForm (ModelForm):
    class Meta:
        model = Citymun
        fields = '__all__'

class VisitorForm (ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

class EstablishmentForm (ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'

class Sys_userForm(ModelForm):
    class Meta:
        model = Sys_user
        fields = '__all__'