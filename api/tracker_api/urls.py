from django.urls import path
from . import views

urlpatterns = [
    path('casesPer100k', views.cases_per_100k),
    path('hesitancyRate', views.hesitancy_rate)
]
