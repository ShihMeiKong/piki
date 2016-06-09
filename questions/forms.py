from django import forms
from .models import Question

class ChoiceCheckbox(forms.Form):
    class Meta:
        model = Question
        fields = ["text"]
        widget = forms.CheckboxSelectMultiple
        # widgets = {
        #     '<field name>':
        # }