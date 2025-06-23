from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm

# Dashboard view - The main page
def dashboard(request):
    income = Transaction.objects.filter(type='IN').aggregate(total=Sum('amount'))['total'] or 0
    expenses = Transaction.objects.filter(type='EX').aggregate(total=Sum('amount'))['total'] or 0
    balance = income - expenses
    recent_transactions = Transaction.objects.all()[:5]
    context = {
        'income': income, 'expenses': expenses, 'balance': balance,
        'recent_transactions': recent_transactions, 'title': 'Dashboard'
    }
    return render(request, 'budget/dashboard.html', context)

# --- Transaction Views ---

def transaction_list(request):
    transactions = Transaction.objects.all()
    transaction_type = request.GET.get('type')
    category_id = request.GET.get('category')
    if transaction_type:
        transactions = transactions.filter(type=transaction_type)
    if category_id:
        transactions = transactions.filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'transactions': transactions, 'categories': categories,
        'title': 'All Transactions'
    }
    return render(request, 'budget/transaction_list.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    category_form = CategoryForm()
    context = {
        'form': form, 'category_form': category_form, 'title': 'Add Transaction'
    }
    return render(request, 'budget/add_transaction.html', context)

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        # Redirect directly to the transaction list page after deletion
        return redirect('transaction_list')
    return render(request, 'budget/transaction_confirm_delete.html', {
        'transaction': transaction, 'title': 'Confirm Deletion'
    })

# --- Category Views ---

def category_list(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    context = {
        'categories': categories, 'form': form, 'title': 'Manage Categories'
    }
    return render(request, 'budget/category_list.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.POST.get('next', 'add_transaction'))
    return redirect(request.POST.get('next', 'add_transaction'))

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form, 'title': f'Edit Category: {category.name}'
    }
    return render(request, 'budget/category_form.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'budget/category_confirm_delete.html', {
        'category': category, 'title': 'Confirm Deletion'
    })
