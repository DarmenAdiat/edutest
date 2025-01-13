from django.core.management.base import BaseCommand
from django.conf import settings
from .models import User, Student  # Импортируйте свои модели

class Command(BaseCommand):
    help = 'Создать объект Student для всех существующих пользователей, если Student ещё не создан.'

    def handle(self, *args, **options):
        users = User.objects.all()
        created_count = 0

        for user in users:
            if not hasattr(user, 'student'):
                Student.objects.create(user=user)
                user.is_student = True
                user.save()
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Успешно создано {created_count} объектов Student.'
        ))
