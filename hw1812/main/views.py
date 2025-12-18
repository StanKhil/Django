from django.shortcuts import render


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


class Reader:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.phone = data['phone']
        self.email = data['email']
        self.created_at = data['created_at']
        self.avatar = data.get('avatar', 'images/default_avatar.jpg')
        self.books = [Book(BOOKS_DB[b_id]) for b_id in data['books']]



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


