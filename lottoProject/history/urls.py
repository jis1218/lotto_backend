"""
URL configuration for lottoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import lottoProject.history.lotto_view
import lottoProject.store.store_view
import lottoProject.statistics.view.statistics_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum_of_balls/', lottoProject.history.lotto_view.sum_of_balls),  # 6개 번호 합
    path('odd_and_even/', lottoProject.history.lotto_view.odd_and_even),  # 짝수 홀수 개수
    path('different_between_first_sixth/', lottoProject.history.lotto_view.different_between_first_sixth),
    # 1번째공, 6번째공 차이
    path('sum_of_1_to_3/', lottoProject.history.lotto_view.sum_of_1_to_3),  # 1~3번째 공 합
    path('sum_of_4_to_6/', lottoProject.history.lotto_view.sum_of_4_to_6),  # 4~6번째 공 합
    path('not_exposed_in_a_row/', lottoProject.history.lotto_view.not_exposed_in_a_row),  # 연속 미출현수
    path('first_lottery_store', lottoProject.store.store_view.first_lottery_store),  # 특정회 1등 당첨점
    path('second_lottery_store', lottoProject.store.store_view.second_lottery_store),  # 특정회 2등 당첨점
    path('nearest_store', lottoProject.store.store_view.nearest_store),  # 내 위치에서 가까운 판매
    path('statistics_menu', lottoProject.statistics.view.statistics_view.statistics_menu),  # 통계 메뉴
]
