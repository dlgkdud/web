from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import templates
from sudoku.models import Ranking
from .api.sudoku import Sudoku
from django.core import serializers
from .models import Ranking

import json
import datetime

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    context = {}
    return render(request, 'sudoku/index.html',context)


def ranking(request):
    context = {}
    return render(request, 'sudoku/ranking.html',context)


def get_ranking_list(request):
    ranking_list = Ranking.objects.order_by('elapsed_time')[:10]
    ranking_data = serializers.serialize("json",ranking_list, fields=('name','elapsed_time'))
    ranking_data = json.loads(ranking_data)
    ranking_data = [{**item['fields'],**{"pk" : item['pk']}} for item in ranking_data]
    ranking_data = {
        "data" : ranking_data
    }
    return JsonResponse(ranking_data)

@csrf_exempt
def register_ranking(request):
    if 'elapsed_time' not in request.session:
        return JsonResponse({'status' : 'failed'})

    data = json.loads(request.body)
    name = data['name']
    elapsed_time = request.session['elapsed_time']

    datetime_args = elapsed_time//3600,(elapsed_time%3600)//60,elapsed_time%60
    d = datetime.time(datetime_args[0], datetime_args[1], datetime_args[2]) 

    ranking = Ranking(name = name, elapsed_time = d)
    ranking.save()

    return JsonResponse({'status' : 'success'})

@csrf_exempt
def check_sudoku(request):
    sudoku_api = Sudoku()

    req_data = json.loads(request.body)
    print(req_data)

    if 'puzzle' not in req_data or 'elapsed_time' not in req_data:
      JsonResponse({'status' : "fail"})

    puzzle = req_data['puzzle']
    elapsed_time = req_data['elapsed_time']

    result = sudoku_api.sudoku_check(puzzle)
    data = {}
    if result == True:
        data['status'] = "clear"
        request.session['status'] = "clear"
        request.session['elapsed_time'] = elapsed_time
    else:
        data['status'] = "fail"

    return JsonResponse(data)


def make_sudoku(request):
    sudoku_api = Sudoku()
    board = sudoku_api.generate_sudoku()
    result = {
        'board' : board
    }

    return JsonResponse(result)



def delete(request) :
    data = Ranking.objects.all()
    data.delete()
    return redirect('ranking')