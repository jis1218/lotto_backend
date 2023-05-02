from peewee import IntegerField, CharField

from lottoProject.config.database_setting import BaseModel


class FirstLotteryStore(BaseModel):
    class Meta:
        db_table = "win_first_lottery_store"

    id = IntegerField()
    round = IntegerField()
    store_name = CharField(max_length=50)
    address = CharField(max_length=100)
    select_type = CharField(max_length=6)
