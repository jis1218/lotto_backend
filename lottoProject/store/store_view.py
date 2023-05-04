import dataclasses

from peewee import JOIN, fn
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json

from rest_framework.utils.encoders import JSONEncoder

from lottoProject.store.dto.win_lottery_info_dto import WinLotteryInfoDto
from lottoProject.store.repository.first_lottery_store import FirstLotteryStore
from lottoProject.store.repository.lotto_store import LottoStore
from lottoProject.store.repository.second_lottery_store import SecondLotteryStore


@api_view(['GET'])
@parser_classes([JSONParser])
def first_lottery_store(request):
    round_number = request.query_params.get('round_number')
    wfls_query = (FirstLotteryStore
                  .select(FirstLotteryStore.address, fn.COUNT(FirstLotteryStore.id).alias('first_lottery'))
                  .group_by(FirstLotteryStore.address)
                  .alias('wfls'))

    print(wfls_query.sql())

    wsls2_query = (SecondLotteryStore
                   .select(SecondLotteryStore.address, fn.COUNT(SecondLotteryStore.id).alias('second_lottery'))
                   .group_by(SecondLotteryStore.address)
                   .alias('wsls2'))

    print(wsls2_query.sql())

    result = (FirstLotteryStore
              .select(FirstLotteryStore, wfls_query.c.first_lottery.alias('first_lottery'),
                      wsls2_query.c.second_lottery.alias('second_lottery'))
              .left_outer_join(wfls_query, on=(FirstLotteryStore.address == wfls_query.c.address))
              .left_outer_join(wsls2_query, on=(FirstLotteryStore.address == wsls2_query.c.address))
              .left_outer_join(LottoStore, on=(FirstLotteryStore.address == LottoStore.address))
              .where(FirstLotteryStore.round == round_number))

    dtos = []
    for my_data in result.dicts():
        print(my_data)
        dto = WinLotteryInfoDto(my_data['round'], my_data['store_name'], my_data['address'], my_data['select_type'],
                                my_data['first_lottery'], my_data['second_lottery'], True)
        dtos.append(dataclasses.asdict(dto))

    json_data = json.dumps(dtos)

    return Response(json_data)


@api_view(['GET'])
@parser_classes([JSONParser])
def second_lottery_store(request):
    round_number = request.query_params.get('round_number')
    wfls_query = (FirstLotteryStore
                  .select(FirstLotteryStore.address, fn.COUNT(FirstLotteryStore.id).alias('first_lottery'))
                  .group_by(FirstLotteryStore.address)
                  .alias('wfls'))

    print(wfls_query.sql())

    wsls2_query = (SecondLotteryStore
                   .select(SecondLotteryStore.address, fn.COUNT(SecondLotteryStore.id).alias('second_lottery'))
                   .group_by(SecondLotteryStore.address)
                   .alias('wsls2'))

    print(wsls2_query.sql())

    result = (SecondLotteryStore
              .select(SecondLotteryStore, wfls_query.c.first_lottery.alias('first_lottery'),
                      wsls2_query.c.second_lottery.alias('second_lottery'))
              .left_outer_join(wfls_query, on=(SecondLotteryStore.address == wfls_query.c.address))
              .left_outer_join(wsls2_query, on=(SecondLotteryStore.address == wsls2_query.c.address))
              .left_outer_join(LottoStore, on=(SecondLotteryStore.address == LottoStore.address))
              .where(SecondLotteryStore.round == round_number))

    dtos = []
    for my_data in result.dicts():
        print(my_data)
        dto = WinLotteryInfoDto(my_data['round'], my_data['store_name'], my_data['address'], my_data['select_type'],
                                my_data['first_lottery'], my_data['second_lottery'], True)
        dtos.append(dataclasses.asdict(dto))

    json_data = json.dumps(dtos)

    return Response(json_data)
