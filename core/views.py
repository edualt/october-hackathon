from django.shortcuts import render
from django.http import JsonResponse


def getRoutes(request):
    routes = [
        '/api/advocates/',
        '/api/companies/',
    ]
    return JsonResponse(routes, safe=False)