from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'})
    )

    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'date', 'category', 'description']
        widgets = {
            'type': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'placeholder': 'e.g., 50.75'}),
            'date': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'placeholder': 'e.g., Weekly grocery shopping'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'placeholder': 'e.g., Utilities'})
        }