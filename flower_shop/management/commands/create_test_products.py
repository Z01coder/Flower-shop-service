from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from flower_shop.models import Product
from pathlib import Path


class Command(BaseCommand):
    """Команда для создания тестовых товаров (bouquet №1-6) с изображениями."""
    
    help = 'Создает тестовые товары (bouquet №1-6) с изображениями из папки tests/assets'

    def handle(self, *args, **options):
        """Основной метод выполнения команды."""
        # Путь к папке с изображениями
        assets_dir = Path(settings.BASE_DIR) / 'flower_shop' / 'tests' / 'assets'
        
        # Создание 6 товаров
        for i in range(1, 7):
            bouquet_name = f'bouquet №{i}'
            price = 2000 + (i - 1) * 500  # От 2000 до 4500 с шагом 500
            image_filename = f'000{i}.webp'
            image_path = assets_dir / image_filename
            
            # Проверка существования файла изображения
            if not image_path.exists():
                self.stdout.write(
                    self.style.ERROR(f'Изображение не найдено: {image_path}')
                )
                continue
            
            # Создание или получение товара
            product, created = Product.objects.get_or_create(
                name=bouquet_name,
                defaults={
                    'price': price,
                    'description': 'test desription'
                }
            )
            
            # Загрузка изображения (если товар был создан или изображение отсутствует)
            if created or not product.image:
                with open(image_path, 'rb') as img_file:
                    product.image.save(
                        image_filename,
                        File(img_file),
                        save=True
                    )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Товар создан: {bouquet_name} (цена: {price} руб.)')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Товар уже существует: {bouquet_name}')
                )

