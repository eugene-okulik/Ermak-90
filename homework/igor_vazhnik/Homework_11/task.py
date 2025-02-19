class Book:
    page_material = 'бумага'
    presence_text = True

    def __init__(self, title, author, number_page, isbn, reserved):
        self.title = title
        self.author = author
        self.number_page = number_page
        self.isbn = isbn
        self.reserved = reserved


    def printed(self):
        if self.reserved:
            print(
                f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_page}, материал: {self.page_material},'
                f' зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_page}, материал: {self.page_material}')


book = Book('Идиот', 'Достоевский', 501, 'asdf', False)
book2 = Book('Идиот2', 'Достоевский', 502, 'asdf', True)
book3 = Book('Идиот3', 'Достоевский', 503, 'asdf', False)
book4 = Book('Идиот4', 'Достоевский', 504, 'asdf', True)
book5 = Book('Идиот5', 'Достоевский', 505, 'asdf', False)

book.reserved = True

book.printed()
book2.printed()
book3.printed()
book4.printed()
book5.printed()


class SchoolTextbooks(Book):

    def __init__(self, title, author, number_page, isbn, reserved, school_subject, school_class, availability_tasks):
        super().__init__(title, author, number_page, isbn, reserved)
        self.school_subject = school_subject
        self.school_class = school_class
        self.availability_tasks = availability_tasks


    def printed(self):
        if self.reserved:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_page}, предмет: '
          f'{self.school_subject}, класс: {self.school_class}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.number_page}, предмет: '
                  f'{self.school_subject}, класс: {self.school_class}')


textBooks = SchoolTextbooks('Математика', 'Иванов', 501, 'asdf', False,
                            'Алгебра', 9, False)
textBooks2 = SchoolTextbooks('Химия', 'Иванов', 501, 'asdf', False,
                             'Химия', 9, False)
textBooks.reserved = True
textBooks.printed()
textBooks2.printed()
