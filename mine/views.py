from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import templates
from mine.models import Ranking
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

@csrf_exempt
def ranking(request):
    context = {}
    return render(request, 'mine/ranking.html',context)

@csrf_exempt
def get_ranking_list(request):
    ranking_list = Ranking.objects.order_by('elapsed_time')[:100]
    ranking_data = serializers.serialize("json",ranking_list, fields=('name','elapsed_time'))
    ranking_data = json.loads(ranking_data)
    ranking_data = [{**item['fields'],**{"pk" : item['pk']}} for item in ranking_data]
    ranking_data = {
        "data" : ranking_data
    }
    return JsonResponse(ranking_data)

@csrf_exempt
def register_ranking(request):

    data = json.loads(request.body)
    print(data)
    if 'elapsed_time' not in data:
        return JsonResponse({'status' : 'failed'})
    name = data['name']
    elapsed_time = data['elapsed_time']

    datetime_args = elapsed_time//3600,(elapsed_time%3600)//60,elapsed_time%60
    d = datetime.time(datetime_args[0], datetime_args[1], datetime_args[2]) 

    ranking = Ranking(name = name, elapsed_time = d)
    ranking.save()

    return JsonResponse({'status' : 'success'})

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

def delete(request) :
    data = Ranking.objects.all()
    data.delete()
    return redirect('ranking')