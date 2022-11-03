from django import forms
from .models import todo

class todoform(forms.ModelForm):
    class Meta:
        model = todo
        fields= ['task','date']
        widgets ={          
            'date': forms.TextInput(attrs={
                'type': 'date',  
            }),
            'task': forms.TextInput(attrs={
                'class': 'form-control',  
            }),
          
        }   
class done(forms.ModelForm):
    
    class Meta:
        model = todo
        fields = ['complted']

class todoupdate(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['task','date','complted']