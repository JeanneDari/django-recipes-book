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
    #servings = int(request.GET.get('servings', 1))
    #return HttpResponse(f'тут будет рецепт омлета, кол-во порций = {servings}')
    context = {
        'omlet': DATA['omlet']
    }
    return render(request, 'omlet.html', context)

def pasta_view(request):
    context = {
        'pasta': DATA['pasta'],
        'servings': int(request.GET.get('servings', 1))
    }
    return render(request, 'demo.html', context)


def buter_view(request):
    context = {
        'buter': DATA['buter']
    }
    return render(request, 'buter.html', context)