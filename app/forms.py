from django import forms

g=[{'MALE','Male'},{'FEMALE','Female'}]
c=[{'PYTHON','Python'},{'DJANGO','Django'},{'SQL','Sql'}]
class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea())
    # gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    # course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.RadioSelect)
    

