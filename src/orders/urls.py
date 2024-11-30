from django.urls import path
from . import views

urlpatterns = [
    path(
        "add",
        views.OrderAddView.as_view(),
        name="order_add"
    ),
    path(
        "list",
        views.OrderListView.as_view(),
        name="order_list"
    ),
    path(
        "detail/<pk>",
        views.OrderDetailView.as_view(),
        name="order_detail"
    ),
]
