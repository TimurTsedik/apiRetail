import yaml
from django.core.management.base import BaseCommand
from ...models import Product, Supplier

class Command(BaseCommand):
    help = 'Import products from a YAML file'

    def handle(self, *args, **kwargs):
        with open('path_to_yaml_file.yaml', 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            supplier = Supplier.objects.get_or_create(name=data['shop'])[0]

            for product in data['goods']:
                Product.objects.create(
                    name=product['name'],
                    supplier=supplier,
                    price=product['price'],
                    quantity=product['quantity'],
                    parameters=product['parameters']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported products'))