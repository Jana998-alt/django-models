from django.urls import path
from .views import SnackListView, snack_detail_view


urlpatterns = [
    path('', SnackListView.as_view(), name = "ListView"),
    path('<int:pk>', snack_detail_view.as_view() , name = "DetailView" ),
    path('snackslist', SnackListView.as_view(), name= 'SnacksList')
]