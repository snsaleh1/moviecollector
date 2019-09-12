from django.forms import ModelForm
from .models import Viewing

class ViewingForm(ModelForm):
  class Meta:
    model = Viewing
    fields = ['date', 'snack']