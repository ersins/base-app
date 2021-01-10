# Yeni uygulamaları bu repodan oluşturuyorum.

# Django uygulaması SECRET_KEY nasıl oluşturulu

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

import secrets

length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
secret_key = ''.join(secrets.choice(chars) for i in range(length))
print(secret_key)
