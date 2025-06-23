from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Transaction URLs
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
]