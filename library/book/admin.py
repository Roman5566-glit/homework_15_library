from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Отображение колонок в списке
    list_display = ('title', 'author', 'price', 'published_date', 'is_available')

    # Фильтры в боковой панели
    list_filter = ('is_available', 'published_date')

    # Поиск по названию и описанию
    search_fields = ('title', 'description')

    # Сортировка: сначала новые книги, затем по названию
    ordering = ('-published_date', 'title')

    # Поля только для чтения (и при создании, и при редактировании)
    readonly_fields = ('price', 'published_date')


# Регистрируем модель в админ-панели
admin.site.register(Book, BookAdmin)
