from django.db import models
from datetime import timedelta

class  Product(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  created_at = models.DateTimeField()
  def __str__(self):
      return self.title