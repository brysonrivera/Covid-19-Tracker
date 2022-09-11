from django.urls import path
from . import views

urlpatterns = [
    path('numCases', views.num_cases),
    path('hesitancyRate', views.hesitancy_rate)
]
