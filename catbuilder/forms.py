from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Cat
        fields = [
            'name',
            # 'image',
            'age',
            'species',
            'hairiness',
            'text'
        ]



