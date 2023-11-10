from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking', views.ranking, name='ranking'),
    path('mine/ranking/register', views.register_ranking, name='register_ranking'),
    path('mine/ranking', views.get_ranking_list, name='get_ranking_list'),
    path('mine/check', views.check_mine, name='check_mine'),
    path('mine/make', views.make_mine, name='make_mine'),
    path('delete', views.delete, name='delete_data'),
]