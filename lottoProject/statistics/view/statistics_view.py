import dataclasses

import json
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from lottoProject.statistics.dto.statistics_menu_dto import StatisticsMenuDto
from lottoProject.statistics.repository.statistics_menu import StatisticsMenu


@api_view(['GET'])
@parser_classes([JSONParser])
def statistics_menu(request):
    statistics_menu_list = StatisticsMenu.select(StatisticsMenu.id, StatisticsMenu.menu_name, StatisticsMenu.order)

    print(statistics_menu_list.sql())

    dtos = []
    for my_data in statistics_menu_list.dicts():
        print(my_data)
        dto = StatisticsMenuDto(my_data['id'], my_data['menu_name'], my_data['order'])
        dtos.append(dataclasses.asdict(dto))

        json_data = json.dumps(dtos, ensure_ascii=False)

    return Response(json_data)