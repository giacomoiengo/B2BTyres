from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import CustomersGroupRequiredMixin
from django.core.paginator import Paginator
from django.views import View
from .forms import ProductFilterForm
from .models import Product
from carts.forms import AddToCartForm
from django.db.models import Q
from django.contrib import messages


class ProductListView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request, page_number):
        q = Q()
        object_list = []
        
        if 'MultipleChoiceFilter' in request.session:
            or_filters = []
            for name, values in request.session['MultipleChoiceFilter'].items():
                q = Q()
                for value in values:
                    q |= Q((name, value))
                or_filters.append(q)
            
            for f in or_filters:
                q &= f

            object_list = Product.objects.filter(q)

        
        form = ProductFilterForm()
        paginator = Paginator(object_list=object_list, per_page=15, allow_empty_first_page=True)
        page = paginator.get_page(page_number)


        return render(request, 'products/product_list.html', {
            'add_to_cart_form'  : AddToCartForm(),
            'customer':request.user.customer,
            'form':form,
            'page':page
        })


    def post(self, request, page_number):
        q = Q()
        form = ProductFilterForm(request.POST)

        
        if form.is_valid():
            request.session['MultipleChoiceFilter'] = form.cleaned_data
            or_filters = []
            for name, values in form.cleaned_data.items():
                q = Q()
                for value in values:
                    q |= Q((name, value))
                or_filters.append(q)
            
            q = Q()
            for f in or_filters:
                q &= f

                
            object_list = Product.objects.filter(q)
            paginator = Paginator(object_list=object_list, per_page=15, allow_empty_first_page=True)
            page = paginator.get_page(1)
        
            return render(request, 'products/product_list.html', {
                'add_to_cart_form'  : AddToCartForm(),
                'customer':request.user.customer,
                'form':form,
                'page':page
            })


            
            
        else:
            messages.error(request, 'Errore')
            return redirect('product_list', 1)

        


class ProductDetailView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request, page_number, pk):
        product = get_object_or_404(Product, pk=pk)

        return render(request, 'products/product_detail.html', {
            'add_to_cart_form'  : AddToCartForm(),
            'product'           : product,
            'customer'          : request.user.customer,
            'page_number'       : page_number,
        })