import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.contrib.auth.hashers import make_password

# Load data from the data.json file
call_command('loaddata', 'data.json')

# Get the CustomUser model
CustomUser = get_user_model()

# Update user instances to be superusers and encrypt passwords
for user in CustomUser.objects.all():
    user.is_superuser = True
    user.is_staff = True
    user.password = make_password(user.password)  # Encrypt the password
    user.save()

print("Superusers created successfully!")