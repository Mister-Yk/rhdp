from django import forms
from .models import Member,Contact,Contribution
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))


class DelegueRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True',
    'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 





class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nom_membre', 'prenom_membre', 'date_of_birth','num_cni', 'num_cei', 'lieu_de_vote', 'contact', 'profession','post_parti', 'image', 'commune', 'departement', 'zone', 'secteur', 'comite']
        widgets = {
            'nom_membre': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_membre': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'num_cni': forms.TextInput(attrs={'class': 'form-control'}),
            'num_cei': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu_de_vote': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'post_parti': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'commune': forms.Select(attrs={'class': 'form-control'}),
            'departement': forms.Select(attrs={'class': 'form-control'}),
            'zone': forms.Select(attrs={'class': 'form-control'}),
            'secteur': forms.Select(attrs={'class': 'form-control'}),
            'comite': forms.Select(attrs={'class': 'form-control'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

class MemberContributionForm(forms.ModelForm):
    nom_membre = forms.CharField(max_length=255)
    mail = forms.EmailField()

    class Meta:
        model = Contribution
        fields = ['sujet', 'text']


class MyPasswordChangeForm(PasswordChangeForm):
    old_password= forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True',
     'autocomplete':'current-password', 'class':'form-control'}))
    new_password1 =forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
     'class':'form-control'}))
    new_password2 =forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
     'class':'form-control'}))
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 =forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
     'class':'form-control'}))
    new_password2 =forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
     'class':'form-control'}))