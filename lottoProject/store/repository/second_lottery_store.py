from peewee import IntegerField, CharField

from lottoProject.config.database_setting import BaseModel


class SecondLotteryStore(BaseModel):
    class Meta:
        db_table = "win_second_lottery_store"

    id = IntegerField()
    round = IntegerField()
    store_name = CharField(max_length=50)
    address = CharField(max_length=100)
