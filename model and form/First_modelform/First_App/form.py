from django import forms
#from First_App.models import First_Table
from First_App import models

class tableform(forms.ModelForm):
    class Meta:
        model=models.First_Table
        fields = "__all__"

class secondform(forms.ModelForm):
    class Meta:
        model=models.Second_table
        fields = "__all__"
        #fields=('First_name','last_Name') # choose korte chasce mane rakte jasce
       # exclude=['First_Name'] # ami jeye field gula bad dete chasce
