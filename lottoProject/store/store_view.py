import dataclasses

from peewee import JOIN, fn
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json

from lottoProject.store.dto.nearest_store_dto import NearestStoreDto
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

    json_data = json.dumps(dtos, ensure_ascii=False)

    return Response(json_data, content_type='text/plain')


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
        dto = WinLotteryInfoDto(my_data['round'], my_data['store_name'], my_data['address'], 'MANUAL',
                                my_data['first_lottery'], my_data['second_lottery'], True)
        dtos.append(dataclasses.asdict(dto))

    json_data = json.dumps(dtos, ensure_ascii=False)

    return Response(json_data)


@api_view(['GET'])
@parser_classes([JSONParser])
def nearest_store(request):
    longitude = request.query_params.get('longitude')
    latitude = request.query_params.get('latitude')
    within = request.query_params.get('distance')

    point = fn.ST_PointFromText(f'POINT({longitude} {latitude})')

    wfls_query = (FirstLotteryStore
                  .select(FirstLotteryStore.address, fn.COUNT(FirstLotteryStore.id).alias('first_lottery'))
                  .group_by(FirstLotteryStore.address)
                  .alias('wfls'))

    wsls2_query = (SecondLotteryStore
                   .select(SecondLotteryStore.address, fn.COUNT(SecondLotteryStore.id).alias('second_lottery'))
                   .group_by(SecondLotteryStore.address)
                   .alias('wsls2'))

    result = (LottoStore
              .select(LottoStore.store_name, LottoStore.address, LottoStore.active, LottoStore.latitude,
                      LottoStore.longitude, fn.ST_Distance_Sphere(LottoStore.location, point).alias('distance'),
                      wfls_query.c.first_lottery.alias('first_lottery'),
                      wsls2_query.c.second_lottery.alias('second_lottery')
                      )
              .left_outer_join(wfls_query, on=(LottoStore.address == wfls_query.c.address))
              .left_outer_join(wsls2_query, on=(LottoStore.address == wsls2_query.c.address))
              .where((fn.ST_Distance_Sphere(LottoStore.location, point) <= within) & (LottoStore.active == True))
              .order_by(fn.alias('distance').asc()))
    dtos = []
    for my_data in result.dicts():
        print(my_data)
        dto = NearestStoreDto(my_data['store_name'], my_data['address'], my_data['longitude'], my_data['latitude'],
                              my_data['distance'], my_data['first_lottery'], my_data['second_lottery'])
        dtos.append(dataclasses.asdict(dto))

    json_data = json.dumps(dtos, ensure_ascii=False)

    return Response(json_data)
