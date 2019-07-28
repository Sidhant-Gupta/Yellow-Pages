from django import forms
from .models import Carpenter,Plumber,Mason,Driver,User,Nurse,Cleaner,Electrician,Cook

class cform(forms.ModelForm):

    class Meta:
        model=Carpenter
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]


class dform(forms.ModelForm):

    class Meta:
        model=Driver
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class pform(forms.ModelForm):
    class Meta:
        model=Plumber
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class mform(forms.ModelForm):
    class Meta:
        model=Mason
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class nform(forms.ModelForm):
    class Meta:
        model=Nurse
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]
class clform(forms.ModelForm):
    class Meta:
        model=Cleaner
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]
class coform(forms.ModelForm):
    class Meta:
        model=Cook
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]
class eform(forms.ModelForm):
    class Meta:
        model=Electrician
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]


class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=[
        "address",

        ]
class filterform(forms.ModelForm):
    class Meta:
        model=User
        fields=[]
