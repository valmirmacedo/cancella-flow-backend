import os
import sys
from pathlib import Path

# Ensure project src directory is in sys.path so 'app' settings module can be imported
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

username = 'valmirmf'
password = '1234'
email = 'valmirmf@example.com'
group_name = 'Admin'

# Ensure group exists
group, _ = Group.objects.get_or_create(name=group_name)

user, created = User.objects.get_or_create(username=username, defaults={'email': email})
if created:
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Created superuser {username}")
else:
    # Update password and flags
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Updated existing user {username}")

# Add to Admin group
user.groups.add(group)
print(f"Added {username} to group {group_name}")
