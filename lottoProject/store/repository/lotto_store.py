from peewee import CharField, TextField, SmallIntegerField, IntegerField

from lottoProject.config.database_setting import BaseModel


class LottoStore(BaseModel):
    class Meta:
        db_table = "lotto_store"

    store_name = CharField(max_length=50)
    location = TextField()
    si = CharField()
    gu = CharField()
    dong = CharField()
    address = CharField()
    active = SmallIntegerField()
    retailer_id = IntegerField()
    longitude = CharField()
    latitude = CharField()
