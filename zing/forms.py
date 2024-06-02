from django import forms
from .models import playlist,songs

class signupf(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

class loginf(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class playlistf(forms.ModelForm):
    class Meta:
        model = playlist
        fields = "__all__"
class songsf(forms.ModelForm):
    class Meta:
        model = songs
        fields = "__all__"

class editf(forms.ModelForm):
    class Meta:
        model = songs
        fields = "__all__"