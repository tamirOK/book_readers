import random
from typing import List

from django.core.management.base import BaseCommand

from core.models import Book, Reader


from mimesis import Datetime, Person, Text


class Command(BaseCommand):
    help = "Inserts test data"

    person_gen = Person("en")
    date_gen = Datetime("en")
    title_gen = Text("en")

    READER_SIZE = 50_000
    BOOK_SIZE = 100_000

    def _get_readers(self):
        return [
            Reader(
                name=self.person_gen.name(),
                birthday=self.date_gen.date(),
            )
            for _ in range(self.READER_SIZE)
        ]

    def _insert_readers(self):
        readers = self._get_readers()
        Reader.objects.bulk_create(readers)

    def _insert_books(self, readers_ids: List[int]):
        books = [
            Book(
                name=self.title_gen.word().capitalize(),
                publish_date=self.date_gen.date(),
                pages=random.randint(50, 1000),
                reader_id=random.choice(readers_ids),
                genre=random.choice(Book.GENRES_LIST)[0]
            )
            for _ in range(self.BOOK_SIZE)
        ]
        Book.objects.bulk_create(books)

    def handle(self, *args, **options):
        # if data insertion hasn't happened
        if Reader.objects.using("master").count() == 0:
            self._insert_readers()
            reader_ids = list(Reader.objects.using("master").values_list("id", flat=True))
            self._insert_books(reader_ids)
