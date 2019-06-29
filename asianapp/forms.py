from django import forms

from asianapp.models import *

class CustomerEmailForms(forms.Form):

    fields=('firstname','lastname','customeremails','customermessage')

    model = CustomerEmail
