from django.contrib import admin
from books_store.models import Book, Profile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
