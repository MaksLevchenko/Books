from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from books_store.forms import BookForm, ProfileForm, UpdateBookForm
from books_store.models import Book, Profile
from books_store.serializers import BookListSerializer, ProfileSerializer


class BooksListView(generics.ListCreateAPIView):
    """Список всех книг"""
    serializer_class = BookListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_list.html'
    permission_classes = [AllowAny]
    form = BookForm
    update_form = UpdateBookForm

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.values(
            *tuple([i.column_name for i in Profile.objects.filter(is_visible=True)]),
            'id'
        )
        return Response({'books': queryset, 'form': self.form,})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return redirect('create')


class ActionView(generics.UpdateAPIView):
    """Изменение отображения"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request, *args, **kwargs):
        list_id = request.POST.getlist('is_visible')
        for item in Profile.objects.all():
            if str(item.id) in list_id:
                item.is_visible = True
            else:
                item.is_visible = False
            item.save()
        return redirect('create')


class UpdateBookView(generics.RetrieveUpdateDestroyAPIView):
    """Обновление книги"""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    lookup_field = 'pk'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return redirect('create')


class DeleteBookView(generics.DestroyAPIView):
    """Удаление книги"""
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    lookup_field = 'pk'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('create')


class ProfileView(APIView):
    """Профиль"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    profile_form = ProfileForm
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return Response({'form': self.profile_form,})
