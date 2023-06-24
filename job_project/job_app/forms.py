from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Offer


# class AddOffer(forms.Form):
#
#     title = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'text'}))
#     category = forms.ChoiceField(choices=Offer.OFFER_CATEGORY)
#     payment = forms.IntegerField(min_value=1)
#     city = forms.CharField(max_length=50)
#     phone = forms.CharField(max_length=20)


class AddOffer(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ('title', 'description', 'category', 'payment', 'city', 'phone')


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
