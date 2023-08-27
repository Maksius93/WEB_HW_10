import psycopg2
import os
import django
from my_app.quotes_app.models import Author, Quote
from decouple import config
from pymongo import MongoClient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_app.my_app.settings")

# Ініціалізуйте Django
django.setup()


# Підключення до MongoDB
m_user = config("MONGO_USER")
m_password = config("MONGO_PASS")
m_domain = config("MONGO_DOMAIN")
m_db_name = config("MONGO_DB_NAME")
mongo_client = MongoClient(f"mongodb+srv://{m_user}:{m_password}@{m_domain}/?retryWrites=true&w=majority")  # Ваше підключення до MongoDB
mongo_db = mongo_client["m_db_name"]

# Зчитування параметрів підключення до PostgreSQL з .env файла або змінних середовища
db_name = config("NAME")
db_user = config("USER")
db_password = config("PASSWORD")
db_host = config("HOST")
db_port = config("PORT")

# Підключення до PostgreSQL
postgres_conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Збереження даних в PostgreSQL
with postgres_conn.cursor() as cursor:
    for mongo_author in mongo_db["authors"].find():
        author = Author.objects.create(
            fullname=mongo_author["fullname"],
            born_date=mongo_author["born_date"],
            born_location=mongo_author["born_location"],
            description=mongo_author["description"]
        )
        for mongo_quote in mongo_db["quotes"].find({"author_id": mongo_author["_id"]}):
            Quote.objects.create(
                quote=mongo_quote["quote"],
                author=author,
                tags=mongo_quote["tags"]
            )

# Закриття з'єднань
mongo_client.close()
postgres_conn.close()
