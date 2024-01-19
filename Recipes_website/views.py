from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def omlet_view(request):
    servings = int(request.GET.get('servings', 1))
    return HttpResponse(f'тут будет рецепт омлета, кол-во порций = {servings}')


def pasta_view(request):
    return HttpResponse('тут будет рецепт пасты')


def hello_view(request):
    return render(request, 'demo.html')
