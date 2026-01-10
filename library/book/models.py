from django.db import models

class Book(models.Model):
    title = models.CharField("Назва", max_length=255)
    author = models.CharField("Автор", max_length=255)
    description = models.TextField("Опис")
    price = models.DecimalField("Ціна", max_digits=10, decimal_places=2)
    stock_count = models.IntegerField("Кількість на складі")
    published_date = models.DateField("Дата публікації")
    is_available = models.BooleanField("В наявності", default=True)

    def __str__(self):
        return self.title
