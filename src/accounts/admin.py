from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import AccountCreationForm, AccountChangeForm
from .models import Account, Supervisor, Salesman, Customer

class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    # list_display = ['email', 'username', 'age', 'is_staff', ] 

admin.site.register(Account,AccountAdmin)
admin.site.register(Supervisor)
admin.site.register(Salesman)
admin.site.register(Customer)
