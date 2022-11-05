from django import forms
from .models import todo
from .models import notes, ideas,goals

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

class notesform(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['title','notes']
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'notes':forms.Textarea(attrs={
                'class':'form-control'
            })
        }

class ideaform(forms.ModelForm):
    
    class Meta:
        model = ideas
        fields = ['ideas']
        widgets = {
            'ideas':forms.TextInput(attrs={
                'class':'form-control'
            })
        }


class goalsform(forms.ModelForm):
    
    class Meta:
        model =goals
        fields = ['goals']
        widgets = {
            'goals':forms.TextInput(attrs={
                'class':'form-control'
            })
        }