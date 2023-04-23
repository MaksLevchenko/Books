from rest_framework import serializers

from books_store.models import Book, Profile


class BookListSerializer(serializers.ModelSerializer):
    """Список книг"""

    class Meta:
        model = Book
        fields = tuple([i.column_name for i in Profile.objects.filter(is_visible=True)])


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""

    class Meta:
        model = Profile
        fields = '__all__'
