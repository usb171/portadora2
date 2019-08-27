from django.urls import path
from .views import *


urlpatterns = [
    path('', Core.login, name='login'),
    path('sala', Core.sala, name='sala'),
    path('getDadosStream', CoreAjax.getDadosStream, name='getDadosStream'),
]