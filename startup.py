import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatpilot.settings')
django.setup()

from django.core.management import call_command

# Run migrations
call_command('migrate')

# Create superuser (replace with your actual credentials)
call_command('createsuperuser', interactive=False,
             username='testing',
             email='testing02@gmail.com',
             password='tester02')
