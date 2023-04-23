from django import forms

from books_store.models import Book, Profile


class BookForm(forms.ModelForm):
    """Форма добавления книги"""

    class Meta:
        model = Book
        fields = ("name", "title", "author", "description", "price")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Это обязательное поле"}),
            "author": forms.TextInput(attrs={"placeholder": "Это обязательное поле"}),
        }


class UpdateBookForm(forms.ModelForm):
    """Форма обновления книги"""

    class Meta:
        model = Book
        fields = ("name", "title", "author", "description", "price")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Это обязательное поле"}),
            "author": forms.TextInput(attrs={"placeholder": "Это обязательное поле"}),
        }


class ProfileForm(forms.ModelForm):
    """Форма управления"""
    is_visible = forms.ModelChoiceField(
        queryset=Profile.objects.all(), widget=forms.CheckboxSelectMultiple, empty_label=None
    )

    class Meta:
        model = Profile
        fields = ("is_visible",)
