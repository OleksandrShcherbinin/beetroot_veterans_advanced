from peewee import *


db = SqliteDatabase('rozetka.db')


class BaseModel(Model):
    class Meta:
        database = db


class Price(BaseModel):
    price = IntegerField()
    old_price = IntegerField(null=True)
    discount = IntegerField()


class Product(BaseModel):
    title = CharField(max_length=255)
    monitor = CharField(default='')
    cpu = CharField(default='')
    memory = CharField(default='')
    drive = CharField(default='')
    price = ForeignKeyField(Price)


class Image(BaseModel):
    product = ForeignKeyField(Product)
    url_link = CharField()


if __name__ == '__main__':
    db.create_tables([Price, Product, Image])
