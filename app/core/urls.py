from django.urls import path
from . import views

urlpatterns = [
    path('check/<nid_number>', views.check_nid)
]
