from .views import ListCreateCab, RetrieveUpdateDelete, ListCreateRider, RetrieveUpdateDeleteRider
from django.urls import path

urlpatterns = [
    path('cabs/', ListCreateCab.as_view(), name='listcabs'),
    path('cabs/<int:pk>', RetrieveUpdateDelete.as_view(), name='getcab'),
    path('rider/', ListCreateRider.as_view(), name='riders'),
    path('rider/<int:pk>', RetrieveUpdateDeleteRider.as_view(), name='rider')
]
