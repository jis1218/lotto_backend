from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import pandas as pd

from lottoProject.history.lotto_history import LottoHistory


@api_view(['GET'])
@parser_classes([JSONParser])
def sum_of_balls(request):
    df = __get_dataframe__()

    row_sums = df.sum(axis=1)

    print(type(row_sums))

    return Response(row_sums)


@api_view(['GET'])
@parser_classes([JSONParser])
def odd_and_even(request):
    df = __get_dataframe__()
    result = {}

    odd_df = df.apply(lambda x: sum(x % 2 != 0), axis=1)
    even_df = df.apply(lambda x: sum(x % 2 == 0), axis=1)

    result_df = pd.concat([odd_df, even_df], axis=1)
    print(result_df)
    print(type(result_df))
    return Response(result_df)


@api_view(['GET'])
@parser_classes([JSONParser])
def different_between_first_sixth(request):
    df = __get_dataframe__()

    print(df['sixth_number'] - df['first_number'])

    return Response(df['sixth_number'] - df['first_number'])


@api_view(['GET'])
@parser_classes([JSONParser])
def sum_of_1_to_3():
    df = __get_dataframe__()

    return Response(df['first_number'] + df['second_number'] + df['third_number'])


@api_view(['GET'])
@parser_classes([JSONParser])
def sum_of_4_to_6():
    df = __get_dataframe__()

    return Response(df['fourth_number'] + df['fifth_number'] + df['sixth_number'])


def __get_dataframe__():
    lotto_histories = LottoHistory.select()

    lotto_histories_dict = [lotto.__data__ for lotto in lotto_histories]

    df = pd.DataFrame(lotto_histories_dict)

    df = df.drop('bonus_number', axis=1)
    df = df.drop('id', axis=1)

    print(df)

    return df
