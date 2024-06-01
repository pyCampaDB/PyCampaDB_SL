# your_app/management/commands/generate_tokens.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generate tokens for all users'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully generated tokens for all users'))
