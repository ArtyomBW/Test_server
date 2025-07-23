from io import BytesIO

import qrcode
from django.core.files.base import ContentFile
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        product = Product.objects.get(id=response.data['id'])
        product.category.products_count += 1
        product.category.save()
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        instance.category.products_count -= 1
        instance.category.save()
        return response


class UserQRcodeCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            qrcode_instance = serializer.save()

            data = (
                f'Fullname : {qrcode_instance.full_name}\n'
                f'Email : {qrcode_instance.email}\n'
                f'Phone : {qrcode_instance.phone_number}',
            )

            qr = qrcode.make(data)  # QR-kodni rasm sifatida yaratadi

            # QR cod ni faylga ogirib , imagefield ga yozish

            buffer = BytesIO()  # Bu — xotirada vaqtinchalik fayl yasaydi.
            qr.save(buffer)  # qr bu biz oldin yaratgan QR code rasmi .save(buffer) bu rasmni xotiradagi buffer ichiga saqlaydi,
            buffer.seek(0)  # ortga qaytarish

            # Fayl nomi
            safe_name = qrcode_instance.full_name.replace(" ", "_")
            filename = f"{safe_name}_qr.png"

            qrcode_instance.qr_code_image.save(
                filename, ContentFile(buffer.getvalue()), save=True
            )

            return Response(UserSerializer(qrcode_instance).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
