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

import lottoProject.lotto_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum_of_balls/', lottoProject.lotto_view.sum_of_balls),
    path('odd_and_even/', lottoProject.lotto_view.odd_and_even),
    path('different_between_first_sixth/', lottoProject.lotto_view.different_between_first_sixth),
    path('sum_of_1_to_3/', lottoProject.lotto_view.sum_of_1_to_3),
    path('sum_of_4_to_6/', lottoProject.lotto_view.sum_of_4_to_6)
]
