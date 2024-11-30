from django.urls import path
from . import views

urlpatterns = [
    path(
        "add/product/<int:page_number>/<pk>",
        views.CartAddProductView.as_view(),
        name="cart_add_product",
    ),
    path(
        "list/product/<int:page_number>",
        views.CartListProductView.as_view(),
        name="cart_list_product",
    ),
    path(
        "delete/product/<int:page_number>/<pk>",
        views.CartDeleteProductView.as_view(),
        name="cart_delete_product",
    ),
]
