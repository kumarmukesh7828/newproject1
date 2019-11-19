from django import forms
from .models import Vendor, VendorAddress


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorAddrForm(forms.ModelForm):
    class Meta:
        model = VendorAddress
        fields = '__all__'

        exclude = ['vendor_id',]
