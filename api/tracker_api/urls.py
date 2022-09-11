from django.urls import path
from . import views

urlpatterns = [
    path('casesPer100k', views.cases_per_100k),
    path('hesitancyRate', views.hesitancy_rate),
    path('communityLevel', views.community_level),
    path('hospitalAdmissionsPer100k', views.hospital_admissions_per_100k)
]
