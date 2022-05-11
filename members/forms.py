from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from members.models import UserProfile


class SingUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileVForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'


class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class CreateProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)