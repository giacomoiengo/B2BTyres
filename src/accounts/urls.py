from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    path('password_change/',lambda x:x, name='password_change'),
    path('password_change/done/',lambda x:x, name='password_change_done'),
    path('password_reset/',lambda x:x, name='password_reset'),
    path('password_reset/done/',lambda x:x, name='password_reset_done'),
    path('reset/<uidb64>/<token>/',lambda x:x, name='password_reset_confirm'),
    path('reset/done/',lambda x:x, name='password_reset_complete'),


    path('salesman/create',      views.SalesmanCreateView.as_view(), name='salesman_create'),
    path('salesman/list',        views.SalesmanListView.as_view(),   name='salesman_list'),
    path('salesman/detail/<pk>', views.SalesmanDetailView.as_view(), name='salesman_detail'),
    path('salesman/update/<pk>', views.SalesmanUpdateView.as_view(), name='salesman_update'),
    path('salesman/delete/<pk>', views.SalesmanDeleteView.as_view(), name='salesman_delete'),


    path('customer/create',      views.CustomerCreateView.as_view(), name='customer_create'),
    path('customer/list',        views.CustomerListView.as_view(),   name='customer_list'),
    path('customer/detail/<pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/update/<pk>', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<pk>', views.CustomerDeleteView.as_view(), name='customer_delete'),


    path('customer/list/onbehalf/<pk_salesman>',   views.CustomerListOnSalesmanBehalfView.as_view(), name='customer_list_on_salesman_behalf'),
    path('customer/detail/<pk>/from/supervisor', views.CustomerDetailFromSupervisorView.as_view(),   name='customer_detail_from_supervisor')

]
