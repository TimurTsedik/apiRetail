# apiRetail

## start DB
docker-compose up -d

## migrations
python manage.py makemigrations
python manage.py migrate

## make user
python manage.py createsuperuser

## run server
python manage.py runserver