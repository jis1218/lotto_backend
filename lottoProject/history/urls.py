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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum_of_balls/', lottoProject.history.lotto_view.sum_of_balls),
    path('odd_and_even/', lottoProject.history.lotto_view.odd_and_even),
    path('different_between_first_sixth/', lottoProject.history.lotto_view.different_between_first_sixth),
    path('sum_of_1_to_3/', lottoProject.history.lotto_view.sum_of_1_to_3),
    path('sum_of_4_to_6/', lottoProject.history.lotto_view.sum_of_4_to_6),
    path('first_lottery_store', lottoProject.store.store_view.first_lottery_store),
    path('second_lottery_store', lottoProject.store.store_view.second_lottery_store),
    path('nearest_store', lottoProject.store.store_view.nearest_store),
]
