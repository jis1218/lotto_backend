import pandas as pd

from history import LottoHistory
from peewee import *
import numpy
import pandas

lotto_histories = LottoHistory.select()

lotto_histories_dict = [lotto.__data__ for lotto in lotto_histories]

df = pd.DataFrame(lotto_histories_dict)

most_frequent_value = df['first_number'].mode().values[0]

df = df.drop('bonus_number', axis=1)
df = df.drop('id', axis=1)
row_sums = df.sum(axis=1)

print(most_frequent_value)

print(row_sums)