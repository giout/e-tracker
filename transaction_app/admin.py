from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'date')


admin.site.register(Transaction, TransactionAdmin)