from django.urls import path
from .views import snack_detail, SnackListView


urlpatterns = [
    path('', SnackListView.as_view(), name = "ListView"),
]