from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from web.models import Borrow

from web.models import Reader, Book


class Command(BaseCommand):
    def handle(self, *args, ** options):
        current_date = now()
        reader = Reader.objects.first()
        book = Book.objects.first()

        for i in range(30):
            current_date -= timedelta(days=1)

            for j in range(randint(5, 10)):
                start_date = current_date + timedelta(hours=randint(0, 10))
                end_date = start_date + timedelta(hours=randint(0, 10))

                Borrow.objects.create(
                    reader= reader,
                    book = book,
                    borrow_date=start_date,
                    return_date=end_date,
                )