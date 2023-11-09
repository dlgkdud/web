from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import templates
# from mine.models import Ranking
from .api.mine import Mine
from django.core import serializers
# from .models import Ranking

import json
import datetime

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    context = {}
    return render(request, 'mine/index.html',context)
    return render(request, 'mine/sol.html',context)


def ranking(request):
  return HttpResponse("ranking view page")


def get_ranking_list(request):
  return HttpResponse("get ranking list page")


def register_ranking(request):
  return HttpResponse("register ranking page")

@csrf_exempt
def check_mine(request):
    mine_api = Mine()
    
    req_data = json.loads(request.body)
    
    puzzle = req_data['puzzle']
    elapsed_time = req_data['elapsed_time']
    
    result = mine_api.open_tile(puzzle)
    data = {}
    if result != 'mine':
        data['status'] = "clear"
        request.session['status'] = "clear"
        request.session['elapsed_time'] = elapsed_time
    else:
        data['status'] = "fail"
    
    return JsonResponse(data)

@csrf_exempt
def make_mine(request):
    mine_api = Mine()
    board = mine_api.generate_mine()
    result = {
        'board' : board
    }

    return JsonResponse(result)