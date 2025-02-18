class Book:
    page_material = 'бумага'
    presence_text = True

    def __init__(self, title, author, number_page, isbn, reserved):
        self.title = title
        self.author = author
        self.number_page = number_page
        self.isbn = isbn
        self.reserved = reserved


book = Book('Идиот', 'Достоевский', 501, 'asdf', False)
book2 = Book('Идиот2', 'Достоевский', 502, 'asdf', True)
book3 = Book('Идиот3', 'Достоевский', 503, 'asdf', False)
book4 = Book('Идиот4', 'Достоевский', 504, 'asdf', True)
book5 = Book('Идиот5', 'Достоевский', 505, 'asdf', False)

book.reserved = True

if book.reserved:
    print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.number_page}, материал: {book.page_material},'
          f' зарезервирована')
else:
    print(f'Название: {book.title}, Автор: {book.author}, страниц: {book.number_page}, материал: {book.page_material}')
# print(book)

if book2.reserved:
    print(f'Название: {book2.title}, Автор: {book2.author}, страниц: {book2.number_page}, материал: '
          f'{book2.page_material}, зарезервирована')
else:
    print(f'Название: {book2.title}, Автор: {book2.author}, страниц: {book2.number_page},  материал: '
          f'{book2.page_material}')

if book3.reserved:
    print(f'Название: {book3.title}, Автор: {book3.author}, страниц: {book3.number_page}, материал: '
          f'{book3.page_material}, зарезервирована')
else:
    print(f'Название: {book3.title}, Автор: {book3.author}, страниц: {book3.number_page},  материал: '
          f'{book3.page_material}')

if book4.reserved:
    print(f'Название: {book4.title}, Автор: {book4.author}, страниц: {book4.number_page}, материал: '
          f'{book4.page_material}, зарезервирована')
else:
    print(f'Название: {book4.title}, Автор: {book4.author}, страниц: {book4.number_page},  материал: '
          f'{book4.page_material}')

if book5.reserved:
    print(f'Название: {book5.title}, Автор: {book5.author}, страниц: {book5.number_page}, материал: '
          f'{book5.page_material}, зарезервирована')
else:
    print(f'Название: {book5.title}, Автор: {book5.author}, страниц: {book5.number_page},  материал: '
          f'{book5.page_material}')


class SchoolTextbooks(Book):

    def __init__(self, title, author, number_page, isbn, reserved, school_subject, school_class, availability_tasks):
        super().__init__(title, author, number_page, isbn, reserved)
        self.school_subject = school_subject
        self.school_class = school_class
        self.availability_tasks = availability_tasks


textBooks = SchoolTextbooks('Математика', 'Иванов', 501, 'asdf', False,
                            'Алгебра', 9, False)
textBooks2 = SchoolTextbooks('Химия', 'Иванов', 501, 'asdf', False,
                            'Химия', 9, False)
textBooks.reserved = True

if textBooks.reserved:
    print(f'Название: {textBooks.title}, Автор: {textBooks.author}, страниц: {textBooks.number_page}, предмет: '
          f'{textBooks.school_subject}, класс: {textBooks.school_class}, зарезервирована')
else:
    print(f'Название: {textBooks.title}, Автор: {textBooks.author}, страниц: {textBooks.number_page}, предмет: '
          f'{textBooks.school_subject}, класс: {textBooks.school_class}')

if textBooks2.reserved:
    print(f'Название: {textBooks2.title}, Автор: {textBooks2.author}, страниц: {textBooks2.number_page}, предмет: '
          f'{textBooks2.school_subject}, класс: {textBooks2.school_class}, зарезервирована')
else:
    print(f'Название: {textBooks2.title}, Автор: {textBooks2.author}, страниц: {textBooks2.number_page}, предмет: '
          f'{textBooks2.school_subject}, класс: {textBooks2.school_class}')
