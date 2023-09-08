from django.db import models
from category_app.models import Category
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) # sets creation date

    def __str__(self):
        return f'{self.amount}$/{self.category}/{self.date}'