from django.core.management.base import BaseCommand
from flower_shop.models import CustomUser


class Command(BaseCommand):
    """Команда для создания тестовых пользователей (админа и обычного пользователя)."""
    
    help = 'Создает тестовых пользователей (админа и обычного пользователя)'

    def handle(self, *args, **options):
        """Основной метод выполнения команды."""
        # Создание админа
        admin, created = CustomUser.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
                'phone': '+79991234567',
                'address': 'Админский адрес'
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(
                self.style.SUCCESS(f'Админ создан: {admin.username} / admin123')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Админ уже существует: {admin.username}')
            )

        # Создание обычного пользователя
        user, created = CustomUser.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'testuser@example.com',
                'phone': '+79997654321',
                'address': 'Тестовый адрес'
            }
        )
        if created:
            user.set_password('test123')
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Пользователь создан: {user.username} / test123')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Пользователь уже существует: {user.username}')
            )

