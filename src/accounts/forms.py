from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, forms, AuthenticationForm


from .models import Supervisor, Salesman, Customer, Account




class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'my-username-class'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'my-password-class'}
    )


class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Account
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = [
            'username',
            # 'password',
            'email',
            # 'first_name',
            # 'last_name',
            'age'
        ]
        labels = {
            'age'  : 'Eta\'',
        }


class AccountChangeForm(UserChangeForm):
    password = None
    
    class Meta(UserChangeForm):
        model = Account
        # fields = UserChangeForm.Meta.fields
        fields = [
            'username',
            # 'password',
            'email',
            # 'first_name',
            # 'last_name',
            'age'
        ]
        labels = {
            'age'  : 'Eta\'',
        }



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = [
            # 'account',
            # 'salesman',
            'markup',
            'discount'
        ]
        labels = {
            'markup'  : 'Ricarico',
            'discount': 'Sconto'
        }

class SalesmanForm(forms.ModelForm):
    class Meta:
        model = Salesman

        fields = [
            # 'account',
            # 'supervisor',
            'city'
        ]
