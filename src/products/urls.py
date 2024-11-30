from django.urls import path
from . import views

urlpatterns = [
    path(
        "list/<int:page_number>",
        views.ProductListView.as_view(),
        name="product_list",
    ),
    path(
        "detail/<int:page_number>/<pk>",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
]
