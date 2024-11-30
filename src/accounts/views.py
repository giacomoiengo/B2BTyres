from email import message
from unicodedata import name
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseForbidden
from .models import Account, Supervisor, Salesman, Customer
from .forms import AccountChangeForm, AccountCreationForm, SalesmanForm, CustomerForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import SupervisorsGroupRequiredMixin, SalesmenGroupRequiredMixin, CustomersGroupRequiredMixin


# Per ottenere i permessi di un modello e attribuirli
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

# Class based views
from django.views.generic import ListView, DetailView
from django.views import View

# Messages
from django.contrib import messages




class CustomerCreateView(LoginRequiredMixin, SalesmenGroupRequiredMixin, View):
    
    def post(self, request):
        account_form = AccountCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)


        if account_form.is_valid() and customer_form.is_valid():
            account = account_form.save()
            account.groups.add(Group.objects.get(name='customers'))
                    
            customer = customer_form.save(commit=False)
            customer.account = account
            customer.salesman = request.user.salesman
            customer.save()
            
            messages.success(request, 'Cliente creato con successo')
            return redirect('customer_detail', customer.pk)
        
        return render(request, 'accounts/customer_create.html', {'account_form' : account_form, 'customer_form' : customer_form})


    def get(self, request):
        return render(request, 'accounts/customer_create.html', {'account_form' : AccountCreationForm(), 'customer_form' : CustomerForm()})



class CustomerListView(LoginRequiredMixin, SalesmenGroupRequiredMixin, View):
    
    def get(self, request):
        object_list = Customer.objects.filter(salesman_id=request.user.salesman.pk)
        return render(request, 'accounts/customer_list.html', {'object_list' : object_list})


class CustomerDetailView(LoginRequiredMixin, SalesmenGroupRequiredMixin, View):
    
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list')

        if customer.salesman_id != request.user.salesman.pk:
            messages.error(request, 'Questo cliente non e\' associato a te!')
            return redirect('customer_list')

        return render(request, 'accounts/customer_detail.html', {'object' : customer})





class CustomerUpdateView(LoginRequiredMixin, SalesmenGroupRequiredMixin, View):
    
    def post(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list')
        

        customer_form = CustomerForm(request.POST, instance=customer)
        account_form = AccountChangeForm(request.POST, instance=customer.account)


        if account_form.is_valid() and customer_form.is_valid():
            account_form.save()
            customer_form.save()
            messages.success(request, 'Cliente modificato con successo')
            return redirect('customer_detail', customer.pk)
         
        return render(request, 'accounts/customer_update.html', {'account_form':account_form, 'customer_form':customer_form})

    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list')

        
        
        customer_form = CustomerForm(instance=customer)
        account_form  = AccountChangeForm(instance=customer.account)

        return render(request, 'accounts/customer_update.html', {'account_form':account_form, 'customer_form':customer_form})
        

class CustomerDeleteView(LoginRequiredMixin, SalesmenGroupRequiredMixin, View):

    def post(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list')

        customer.account.delete()
        # customer.delete()

        messages.success(request, 'Cliente eliminato con successo')
        return redirect('customer_list')

    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list')

        return render(request, 'accounts/customer_delete.html', {'customer': customer})




















class SalesmanCreateView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):


    def post(self, request):
        account_form = AccountCreationForm(request.POST)
        salesman_form = SalesmanForm(request.POST)


        if account_form.is_valid() and salesman_form.is_valid():
            account = account_form.save()
            account.groups.add(Group.objects.get(name='salesmen'))
        

            salesman = salesman_form.save(commit=False)
            salesman.account = account
            salesman.supervisor = request.user.supervisor
            salesman.save()
            
            messages.success(request, 'Rappresentante creato con successo')
            return redirect('salesman_detail', salesman.pk)
        
        return render(request, 'accounts/salesman_create.html', {'account_form' : account_form, 'salesman_form' : salesman_form})


    def get(self, request):
        return render(request, 'accounts/salesman_create.html', {'account_form' : AccountCreationForm(), 'salesman_form' : SalesmanForm()})









class SalesmanListView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):
    
    def get(self, request):
        object_list = Salesman.objects.filter(supervisor_id=request.user.supervisor.pk)
        return render(request, 'accounts/salesman_list.html', {'object_list' : object_list})


class SalesmanDetailView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):
    
    def get(self, request, pk):
        try:
            salesman = Salesman.objects.get(pk=pk)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')

        if salesman.supervisor_id != request.user.supervisor.pk:
            messages.error(request, 'Questo rappresentante non e\' associato a te!')
            return redirect('salesman_list')

        return render(request, 'accounts/salesman_detail.html', {'object' : salesman})

    



class SalesmanUpdateView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):

    def post(self, request, pk):
        try:
            salesman = Salesman.objects.get(pk=pk)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')
        

        salesman_form = SalesmanForm(request.POST, instance=salesman)
        account_form = AccountChangeForm(request.POST, instance=salesman.account)


        if account_form.is_valid() and salesman_form.is_valid():
            account_form.save()
            salesman_form.save()
            messages.success(request, 'Rappresentante modificato con successo')
            return redirect('salesman_detail', salesman.pk)
        
        
        return render(request, 'accounts/salesman_update.html', {'account_form':account_form, 'salesman_form':salesman_form})

    def get(self, request, pk):
        try:
            salesman = Salesman.objects.get(pk=pk)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')

        
        
        salesman_form = SalesmanForm(instance=salesman)
        account_form  = AccountChangeForm(instance=salesman.account)

        return render(request, 'accounts/salesman_update.html', {'account_form':account_form, 'salesman_form':salesman_form})
        

class SalesmanDeleteView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):
    
    def post(self, request, pk):
        try:
            salesman = Salesman.objects.get(pk=pk)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')

        salesman.account.delete()
        # salesman.delete()

        messages.success(request, 'Rappresentante eliminato con successo')
        return redirect('salesman_list')

    def get(self, request, pk):
        try:
            salesman = Salesman.objects.get(pk=pk)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')

        return render(request, 'accounts/salesman_delete.html', {'salesman': salesman})

        

class CustomerListOnSalesmanBehalfView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):
    
    def get(self, request, pk_salesman):
        try:
            salesman = Salesman.objects.get(pk=pk_salesman)
        except Salesman.DoesNotExist:
            messages.error(request, 'Questo rappresentante non esiste!')
            return redirect('salesman_list')

        if salesman.supervisor_id != request.user.supervisor.pk:
            messages.error(request, 'Questo rappresentante non e\' associato a te!')
            return redirect('salesman_list')


        object_list = Customer.objects.filter(salesman_id=salesman.pk)
        return render(request, 'accounts/customer_list_on_salesman_behalf.html', {'object_list' : object_list, 'pk_salesman' : pk_salesman})

# Supervisori accedono, non rappresentanti
class CustomerDetailFromSupervisorView(LoginRequiredMixin, SupervisorsGroupRequiredMixin, View):
    
    def get(self, request, pk):        
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            messages.error(request, 'Questo cliente non esiste!')
            return redirect('customer_list_on_salesman_behalf')

        if customer.salesman.supervisor_id != request.user.supervisor.pk:
            messages.error(request, 'Questo cliente non e\' associato ad un rappresentante associato a te!')
            return redirect('customer_list_on_salesman_behalf')

        return render(request, 'accounts/customer_detail_from_supervisor.html', {'object' : customer})
