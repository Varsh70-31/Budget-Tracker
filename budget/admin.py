from django.contrib import admin
from .models import Category, Transaction

# Register models to make them accessible in the Django admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'amount', 'category', 'description')
    list_filter = ('type', 'category', 'date')
    search_fields = ('description', 'category__name')
    date_hierarchy = 'date'