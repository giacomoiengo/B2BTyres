from django.shortcuts import render, redirect, get_object_or_404
from django.views import View



from .models import Product, Cart, Cart_Product


from .forms import AddToCartForm
from django.contrib import messages


from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import CustomersGroupRequiredMixin






class CartAddProductView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def post(self, request, page_number, pk):
        
        cart , created = Cart.objects.get_or_create(customer=request.user.customer)

        product = get_object_or_404(Product, pk=pk)

        form = AddToCartForm(request.POST)
        
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            if quantity > product.stock:
                messages.error(request, 'Quantita\' richiesta maggiore della disponibilita\'')
                return redirect('product_list', page_number)


            relation , created = Cart_Product.objects.update_or_create(cart=cart, product=product)
            relation.quantity = quantity
            relation.save() 

            messages.success(request, f"Aggiunti {quantity} elementi.")
            return redirect('product_list', page_number)


        else:
            messages.error(request, 'Form non valido!')
            return redirect('product_list', page_number)


class CartListProductView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request, page_number):
        cart , created = Cart.objects.get_or_create(customer=request.user.customer)
        cart_product = Cart_Product.objects.filter(cart=cart)
        return render(request, 'carts/cart_list.html', {
            'cart'          : cart,
            'cart_product'  : cart_product,
            'page_number'   : page_number
        })

class CartDeleteProductView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request, page_number, pk):
        cart , created = Cart.objects.get_or_create(customer=request.user.customer)
        relation = get_object_or_404(Cart_Product, cart=cart, product_id=pk)
        relation.delete()
        messages.success(request, 'Prodotto eliminato.')
        return redirect('cart_list_product', page_number)


        
        


