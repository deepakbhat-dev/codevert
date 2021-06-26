from django import forms
from .models import SUPPORTED_LANG

class InputForm(forms.Form):
    input_text = forms.CharField( label='', max_length=6000, required=False,
        widget=forms.Textarea(attrs={'width':"100%", 'cols' : "68", 'rows': "13",
          'style':"font-size: large; font-weight:550; padding-left: 10px; padding-right: 10px;",
             'placeholder':'Enter Data for Detection', }) )

    def clean_input_text(self):
        if self.cleaned_data['input_text'].strip() == '':
            raise forms.ValidationError('Please enter string to detect!')
        return self.cleaned_data['input_text']
