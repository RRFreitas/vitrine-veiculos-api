docker pull postgres
docker run -p 5432:5432 -v /tmp/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres

python manage.py migrate
python manage.py createsuperuser --email admin@admin.com --username admin


