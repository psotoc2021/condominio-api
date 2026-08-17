import os

from django.contrib.auth import get_user_model


User = get_user_model()

username = os.environ.get("DJANGO_INITIAL_USERNAME")
password = os.environ.get("DJANGO_INITIAL_PASSWORD")

if username and password:
    user, created = User.objects.get_or_create(username=username)

    if created:
        user.set_password(password)
        user.save()
        print(f"Initial user '{username}' created.")
    else:
        print(f"Initial user '{username}' already exists.")
else:
    print("Initial user variables not configured. Skipping user creation.")