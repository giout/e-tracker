from django.db import models
from category_app.models import Category

class Transaction(models.Model):
    amount = models.FloatField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) # sets creation date

    def __str__(self):
        return f'{self.amount}$/{self.category}/{self.date}'