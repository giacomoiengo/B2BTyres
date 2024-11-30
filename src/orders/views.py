from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from carts.models import Cart, Cart_Product
from orders.models import Order, Order_Product

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import CustomersGroupRequiredMixin

class OrderAddView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def post(self, request):

        cart = get_object_or_404(Cart, customer=request.user.customer) 

        relations = Cart_Product.objects.filter(cart=cart)

        if not bool(relations):
            messages.error(request, 'Nulla da ordinare!')
            return redirect('cart_list_product', 1)

        order = Order(
            customer = request.user.customer,
            customer_markup = request.user.customer.markup,
            customer_discount = request.user.customer.discount,
        )
        order.save()

        for relation in relations:
            Order_Product(
                order = order,
                product = relation.product,
                product_quantity = relation.quantity,
                product_price    = relation.product.price,
                product_price_adjusted = relation.product.adjust_price(request.user.customer),
            ).save()
        
        Cart_Product.objects.filter(cart=cart).delete()
        messages.success(request, 'Ordine creato con successo!')
        return redirect('cart_list_product', 1)


class OrderListView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request):
        data = []
        for order in Order.objects.filter(customer=request.user.customer):
            data.append((
                order, 
                Order_Product.objects.filter(order=order)
            ))
        
        return render(request, 'orders/order_list.html', {'order_relations':data})

class OrderDetailView(LoginRequiredMixin, CustomersGroupRequiredMixin, View):
    def get(self, request):
        pass


        

        
        


