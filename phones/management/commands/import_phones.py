import csv

from django.core.management.base import BaseCommand
from django.http import HttpResponse
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                phone = Phone(
                    id=phone["id"],
                    name=phone["name"],
                    image=phone["image"],
                    price=phone["price"],
                    release_date=phone["release_date"],
                    lte_exists=phone["lte_exists"],
                    slug=phone['name'].lower().replace(' ', '-'))
                print(phone.slug)
                phone.save()





