from django.urls import path
from .views import account_list, account_detail, Create, Update, Delete



urlpatterns = [
    path('', account_list),
    path('create/', Create),
    path('<account_email>/', account_detail),   
    path('<account_id>/update/', Update),
    path('<account_id>/delete/', Delete),
]