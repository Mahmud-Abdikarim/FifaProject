from django import forms

class ClubForm(forms.Form):
    #clubid = forms.IntegerField(label='Club id')
    club_name = forms.CharField(label='Club name', max_length=200)
    leagueid = forms.IntegerField(label='League id')