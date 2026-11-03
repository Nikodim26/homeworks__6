from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = "Проверяет работу Redis через Django cache"

    def handle(self, *args, **options):
        # Пытаемся получить данные из кеша
        data = cache.get('my_key')

        if not data:
            self.stdout.write(self.style.WARNING('Данные не найдены в кеше, выполняем вычисления...'))
            data = 'some expensive computation'
            cache.set('my_key', data, 60 * 5)  # Кешируем на 15 минут
        else:
            self.stdout.write(self.style.SUCCESS('Данные получены из кеша!'))

        # Выводим реальные данные, а не строку 'data'
        self.stdout.write(f'Результат: {data}')
