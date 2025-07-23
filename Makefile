mig:
	python manage.py makemigrations
	python manage.py migrate


Fix_up:
	make product-json # Json activate cod

Fix_cat:
	python manage.py dumpdata apps.Category --indent 4 > category.json # Category uchun JSON fayl yaratish

Fix_pro:
	python manage.py dumpdata apps.Product --indent 4 > product.json # Product uchun JSON fayl yaratish

bots:
	python bot/main.py
