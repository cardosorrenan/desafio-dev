from django.urls import path
from . import views

urlpatterns = [
    path('', views.stores, name='stores'),
    path('stores/<int:store_id>/transactions/', views.stores_transactions, name='transactions_store'),
    path('upload_cnab', views.upload_cnab, name='upload_cnab'),
    path('manage_cnab', views.manage_cnab, name='manage_cnab'),
]