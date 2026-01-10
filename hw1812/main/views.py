from django.shortcuts import redirect, render, get_object_or_404
from main.forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.contrib import messages
import os
from django.conf import settings

def save_file(file, folder):
    fs = FileSystemStorage(location=f'media/{folder}')
    filename = fs.save(file.name, file)
    return f'{folder}/{filename}'

def delete_file(file_path):
    if not file_path:
        return

    if file_path.startswith('images/'):
        return

    full_path = os.path.join(settings.MEDIA_ROOT, file_path)

    if os.path.exists(full_path):
        os.remove(full_path)


def books_list(request):
    show_available = request.GET.get('available')

    if show_available == '1':
        books = Book.objects.filter(is_available=True)
    else:
        books = Book.objects.all()

    return render(request, 'books/index.html', {'books': books, 'show_available': show_available})


@login_required
@permission_required('main.view_book', raise_exception=True)
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.image = f'images/book{pk}.jfif'
    return render(request, 'books/details.html', {'book': book})


@login_required
@permission_required('main.view_reader', raise_exception=True)
def readers_list(request):
    readers = Reader.objects.prefetch_related('books')
    return render(request, 'readers/index.html', {'readers': readers})

@login_required
@permission_required('main.view_reader', raise_exception=True)
def reader_details(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    return render(request, 'readers/details.html', {'reader': reader})



@login_required
@permission_required('main.add_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                year=form.cleaned_data['year'],
                genre=form.cleaned_data['genre'],
                publisher=form.cleaned_data['publisher'],
                is_available=form.cleaned_data['is_available'],
                cover=form.cleaned_data.get('cover')
            )
            return redirect('books_list')
    else:
        form = BookForm()

    return render(request, 'books/form.html', {'form': form})



@login_required
@permission_required('main.change_book', raise_exception=True)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                if value is not None:
                    setattr(book, field, value)
            book.save()
            return redirect('book_details', pk=pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'books/form.html', {'form': form})



@login_required
@permission_required('main.delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        if book.cover:
            delete_file(book.cover.name)
        book.delete()
        return redirect('books_list')

    return render(request, 'books/delete.html', {'book': book})




@login_required
@permission_required('main.add_reader', raise_exception=True)
def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST, request.FILES)
        form.fields['books'].choices = [(b.id, b.title) for b in Book.objects.all()]

        if form.is_valid():
            reader = Reader.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                avatar=form.cleaned_data.get('avatar')
            )
            reader.books.set(form.cleaned_data['books'])
            return redirect('readers_list')
    else:
        form = ReaderForm()
        form.fields['books'].choices = [(b.id, b.title) for b in Book.objects.all()]

    return render(request, 'readers/form.html', {'form': form})



@login_required
@permission_required('main.change_reader', raise_exception=True)
def reader_update(request, pk):
    reader = get_object_or_404(Reader, pk=pk)

    if request.method == 'POST':
        form = ReaderForm(request.POST, request.FILES)
        form.fields['books'].choices = [(b.id, b.title) for b in Book.objects.all()]

        if form.is_valid():
            reader.first_name = form.cleaned_data['first_name']
            reader.last_name = form.cleaned_data['last_name']
            reader.phone = form.cleaned_data['phone']
            reader.email = form.cleaned_data['email']

            if form.cleaned_data.get('avatar'):
                reader.avatar = form.cleaned_data['avatar']

            reader.save()
            reader.books.set(form.cleaned_data['books'])
            return redirect('readers_list')
    else:
        form = ReaderForm(instance=reader)
        form.fields['books'].choices = [(b.id, b.title) for b in Book.objects.all()]

    return render(request, 'readers/form.html', {'form': form})


@login_required
@permission_required('main.delete_reader', raise_exception=True)
def reader_delete(request, pk):
    reader = get_object_or_404(Reader, pk=pk)

    if request.method == 'POST':
        if reader.avatar:
            delete_file(reader.avatar.name)
        reader.delete()
        return redirect('readers_list')

    return render(request, 'readers/delete.html', {'reader': reader})


