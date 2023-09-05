from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.description