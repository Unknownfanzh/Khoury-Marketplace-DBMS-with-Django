from django import forms

class SQLQueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea, label='Enter your SQL query here')
