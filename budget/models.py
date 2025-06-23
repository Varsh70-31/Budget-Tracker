from django.db import models
from django.utils.timezone import now

# Model for transaction categories
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Enter a transaction category (e.g. Groceries, Salary)")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

# Model for transactions (both income and expenses)
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Income'),
        ('EX', 'Expense'),
    ]

    type = models.CharField(max_length=2, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255, help_text="A brief description of the transaction.")

    class Meta:
        ordering = ['-date'] # Show newest transactions first

    def __str__(self):
        return f"{self.get_type_display()} of {self.amount} on {self.date}"