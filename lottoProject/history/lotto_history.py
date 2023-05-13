from peewee import IntegerField, PrimaryKeyField

from lottoProject.config.database_setting import BaseModel


class LottoHistory(BaseModel):
    class Meta:
        db_table = "lotto_win_number_history"
    # draw_date = DateField()
    round = PrimaryKeyField()
    first_number = IntegerField()
    second_number = IntegerField()
    third_number = IntegerField()
    fourth_number = IntegerField()
    fifth_number = IntegerField()
    sixth_number = IntegerField()
    bonus_number = IntegerField()

