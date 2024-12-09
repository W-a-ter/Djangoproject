from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # наполняем таблицу категории данными о категории
        category, _ = Category.objects.get_or_create(name='ГовардВоловиц', description='Астрофизик')

        # Продукты категории
        products = [
            {'name': 'Манишка', 'description': 'вязанная, красная', 'category': category, 'price': 1500},
            {'name': 'мопед', 'description': '2 колеса', 'category': category, 'price': 3000},
        ]

        # циклом выполняем команду заполнения таблицу продуктов данными
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
