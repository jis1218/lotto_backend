from peewee import MySQLDatabase, Model

db = MySQLDatabase('insup', user='root', password='amadeus21!', host='localhost', port=3309)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db
