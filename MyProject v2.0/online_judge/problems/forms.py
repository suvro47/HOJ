from django import forms
from submissions.models import Submission

Language_Choices = [
    ('C', 'C'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Python 3', 'Python 3'),
    ]


class SubmitForm(forms.Form):
    language = forms.CharField(widget=forms.Select(choices=Language_Choices))
    solution = forms.FileField()

    class Meta:
        model = Submission
        fields = ('language', 'solution',)

