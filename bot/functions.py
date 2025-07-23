import os
import sys

import qrcode
from django.core.files.base import ContentFile

from bot.utils import generate_qr_code_image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')


import django
django.setup()


from asgiref.sync import sync_to_async
from apps.models import User

@sync_to_async
def save_user_to_db(**kwargs):
    user = User.objects.filter(user_id=kwargs['user_id']).first()

    if user.exists():
        qr_image = generate_qr_code_image(str(kwargs['user_id']))
        new_user = User.objects.create(
            full_name=kwargs['full_name'],
            email=kwargs['email'],
            user_id=kwargs['user_id'],
        )
        new_user.qr_code.save("qrcode.png", qr_image)





