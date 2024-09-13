from django import forms

class SurveyForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.CheckboxInput)
    views = forms.IntegerField(widget=forms.TextInput)
    available = forms.BooleanField(widget=forms.TextInput)
    date = forms.DateField(widget=forms.SelectDateWidget)