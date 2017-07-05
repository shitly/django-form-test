from django import forms

from news.models import Categary


class SearchForm(forms.Form):
    serach_start = forms.DateField(label = "开始时间")
    serach_end = forms.DateField(label = "结束时间")
    tag = forms.ModelChoiceField(label=u"栏目", queryset=Categary.objects.all())
    title_word = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'id': 'title_word',
                   'placeholder': '模糊标题(支持正则搜索)',
                   }),
    )
    # a = forms.CheckboxInput()


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class TwoMenberDateForm(forms.Form):
    serach_start = forms.DateField(
        widget = forms.DateInput(
            attrs={'class': ['form-control', 'vDateField'],
                   'id': 'serach_start',
                   }),
    )
    serach_end = forms.DateField(
        widget = forms.DateInput(
            attrs={'class': ['form-control', 'vDateField'],
                   'id': 'serach_end',
                   }),
    )









