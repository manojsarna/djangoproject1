# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('un_dashboard', views.un_dashboard, name='un_dashboard'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
