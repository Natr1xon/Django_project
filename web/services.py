import csv

from web.models import Borrow

from web.models import Reader, Book


def filter_borrow_book(book_qs, filters: dict):
    if filters['search']:
        book_qs = book_qs.filter(book=filters['search'])

    if filters['borrow_date']:
        book_qs = book_qs.filter(borrow_date__gte = filters['borrow_date'])

    if filters['return_date']:
        book_qs = book_qs.filter(borrow_date__lte = filters['return_date'])
    return book_qs

def export_book_csv(book_qs, responce):
    writer = csv.writer(responce)
    writer.writerow(("reader","book","borrow_date","return_date"))

    for book in book_qs:
        writer.writerow((book.reader,book.book,book.borrow_date,book.return_date))

    return responce

def import_book_from_csv(file):
    strs_from_file = (row.decode() for row in file)
    reader = csv.DictReader(strs_from_file)

    borrow = []
    for row in reader:
        reader_instance = Reader.objects.get(firstname=row["reader"].split()[0], lastname=row["reader"].split()[1])
        book_instance = Book.objects.get(title=row["book"])

        borrow.append(Borrow(
            reader=reader_instance,
            book=book_instance,
        ))

    Borrow.objects.bulk_create(borrow)