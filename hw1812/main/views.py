from django.shortcuts import redirect, render
from main.forms import *
from django.core.files.storage import FileSystemStorage
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



BOOKS_DB = {
    1: {
        'id': 1,
        'title': 'Гамлет',
        'author': 'Вільям Шекспір',
        'year': 1603,
        'genre': 'Трагедія',
        'publisher': 'Нілсон',
        'is_available': True,
    },
    2: {
        'id': 2,
        'title': '1984',
        'author': 'Джордж Орвелл',
        'year': 1949,
        'genre': 'Антиутопія',
        'publisher': 'Secker & Warburg',
        'is_available': False,
    }
}

READERS_DB = {
    1: {
        'id': 1,
        'first_name': 'Іван',
        'last_name': 'Петренко',
        'phone': '+380991112233',
        'email': 'ivan@test.com',
        'created_at': '2024-01-10',
        'books': [2],
        'avatar': 'images/reader1.jfif',
    },
    2: {
        'id': 2,
        'first_name': 'Олена',
        'last_name': 'Коваль',
        'phone': '+380501234567',
        'email': 'olena@test.com',
        'created_at': '2024-02-05',
        'books': [],
        'avatar': 'images/reader2.jfif',
    }
}


class Book:
    def __init__(self, data: dict):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.year = data['year']
        self.genre = data['genre']
        self.publisher = data['publisher']
        self.is_available = data['is_available']
        self.cover = data.get('cover')


class Reader:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone = data['phone']
        self.email = data['email']
        self.created_at = data['created_at']
        self.avatar = data.get('avatar')
        self.books = [Book(BOOKS_DB[int(b_id)]) for b_id in data['books']]



def books_list(request):
    books = [Book(book) for book in BOOKS_DB.values()]
    return render(request, 'books/index.html', {'books': books})


def book_details(request, pk):
    book = Book(BOOKS_DB[pk])
    book.image = f'images/book{pk}.jfif'
    return render(request, 'books/details.html', {'book': book})



def readers_list(request):
    readers = [Reader(reader) for reader in READERS_DB.values()]
    return render(request, 'readers/index.html', {'readers': readers})


def reader_details(request, pk):
    reader = Reader(READERS_DB[pk])
    return render(request, 'readers/details.html', {'reader': reader})



def books_list(request):
    books = [Book(book) for book in BOOKS_DB.values()]
    return render(request, 'books/index.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            cover_path = None
            if data.get('cover'):
                cover_path = save_file(data['cover'], 'books')

            BOOKS_DB[data['id']] = {
                'id': data['id'],
                'title': data['title'],
                'author': data['author'],
                'year': data['year'],
                'genre': data['genre'],
                'publisher': data['publisher'],
                'is_available': data['is_available'],
                'cover': cover_path or 'images/default_book.jpg',
            }
            return redirect('books_list')
    else:
        form = BookForm()

    return render(request, 'books/form.html', {'form': form})


def book_update(request, pk):
    book = BOOKS_DB[pk]

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            if data.get('cover'):
                book['cover'] = save_file(data['cover'], 'books')

            for field in ['title', 'author', 'year', 'genre', 'publisher', 'is_available']:
                book[field] = data[field]

            return redirect('book_details', pk=pk)
    else:
        form = BookForm(initial=book)

    return render(request, 'books/form.html', {'form': form})


def book_delete(request, pk):
    if request.method == 'POST':
        book = BOOKS_DB.get(pk)

        if book:
            delete_file(book.get('cover'))
            BOOKS_DB.pop(pk)

        return redirect('books_list')

    return render(request, 'books/delete.html', {'id': pk})




def reader_create(request):
    book_choices = [(k, v['title']) for k, v in BOOKS_DB.items()]

    if request.method == 'POST':
        form = ReaderForm(request.POST, request.FILES)
        form.fields['books'].choices = book_choices

        if form.is_valid():
            data = form.cleaned_data

            avatar_path = 'images/default_avatar.jpg'
            if data.get('avatar'):
                avatar_path = save_file(data['avatar'], 'readers')

            READERS_DB[data['id']] = {
                'id': data['id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'phone': data['phone'],
                'email': data['email'],
                'created_at': data['created_at'],
                'books': data['books'],
                'avatar': avatar_path,
            }
            return redirect('readers_list')
    else:
        form = ReaderForm()
        form.fields['books'].choices = book_choices

    return render(request, 'readers/form.html', {'form': form})


def reader_update(request, pk):
    reader = READERS_DB[pk]
    book_choices = [(k, v['title']) for k, v in BOOKS_DB.items()]

    if request.method == 'POST':
        form = ReaderForm(request.POST, request.FILES)
        form.fields['books'].choices = book_choices

        if form.is_valid():
            data = form.cleaned_data

            if data.get('avatar'):
                reader['avatar'] = save_file(data['avatar'], 'readers')

            for field in ['first_name', 'last_name', 'phone', 'email', 'created_at', 'books']:
                reader[field] = data[field]

            return redirect('reader_details', pk=pk)
    else:
        form = ReaderForm(initial=reader)
        form.fields['books'].choices = book_choices

    return render(request, 'readers/form.html', {'form': form})



def reader_delete(request, pk):
    if request.method == 'POST':
        reader = READERS_DB.get(pk)

        if reader:
            delete_file(reader.get('avatar'))
            READERS_DB.pop(pk)

        return redirect('readers_list')

    return render(request, 'readers/delete.html', {'id': pk})

