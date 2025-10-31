from django.urls import path
from meem.views import check_age, regions

urlpatterns = [
    path('check-age/', check_age, name='check_age'),
    path('regions/', regions, name='regions'),
]