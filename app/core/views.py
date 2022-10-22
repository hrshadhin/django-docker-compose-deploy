from django.shortcuts import render
from django.http import JsonResponse
from .models import NIDInfo
from rest_framework.decorators import api_view


@api_view()
def check_nid(request, nid_number):
    is_exist = NIDInfo.objects.filter(nid_number=nid_number).exists()
    return JsonResponse({'status': is_exist})
