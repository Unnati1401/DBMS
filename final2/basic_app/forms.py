from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Bloodbank,Stock,BloodCamps
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('first_name','last_name','username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields=('City','DOB','No_of_donations')

class BloodBankForm(forms.ModelForm):
    class Meta():
        model=Bloodbank
        fields="__all__"

class EditProfileForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

class StockUpdateForm(forms.ModelForm):
    class Meta():
        model = Stock
        fields = ('Bid','Number_of_bags','Blood_component','Blood_group','Cost')

class CampsForm(forms.ModelForm):
    class Meta():
        model=BloodCamps
        fields = "__all__"
