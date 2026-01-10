from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Відображення колонок у списку
    list_display = ('title', 'author', 'price', 'published_date', 'is_available')

    # Фільтри у боковій панелі
    list_filter = ('is_available', 'published_date')

    # Пошук по назві та опису
    search_fields = ('title', 'description')

    # Сортування: спочатку нові книги, потім за назвою
    ordering = ('-published_date', 'title')

    # Поля тільки для читання **тільки при редагуванні**
    def get_readonly_fields(self, request, obj=None):
        if obj:  # якщо редагуємо існуючий об’єкт
            return ('price', 'published_date')
        return ()  # при створенні книги всі поля доступні для редагування

# Реєструємо модель у адмінці
admin.site.register(Book, BookAdmin)
