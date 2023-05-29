from peewee import IntegerField, CharField

from lottoProject.config.database_setting import BaseModel


class StatisticsMenu(BaseModel):
    class Meta:
        db_table = "statistics_menu"

    id = IntegerField()
    menu_name = CharField(max_length=30)
    order = IntegerField()
