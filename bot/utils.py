import qrcode
from django.core.files import File
from io import BytesIO


def generate_qr_code_image(data: str):
    qr= qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    return File(buffer, name="qrcode.png")