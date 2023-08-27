import pymongo
import psycopg2
from django.db import transaction
from my_app.quotes_app.models import Author, Quote
from django.conf import settings



# Підключення до MongoDB
mongo_client = pymongo.MongoClient(settings.MONGO_URI)
mongo_db = mongo_client[settings.MONGO_DBNAME]


# Збереження даних в PostgreSQL
with transaction.atomic():
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

