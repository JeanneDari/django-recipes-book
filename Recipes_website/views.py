from django.shortcuts import render

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


def dish_view(request, dish):
    quantity = int(request.GET.get('servings', 1))
    new_dic = {}
    ingr = list(DATA[dish].keys())
    q = list(DATA[dish].values())
    for i, ingredient in enumerate(ingr):
        new_dic[ingredient] = q[i] * quantity
    context = {'Рецепт': f'Рецепт блюда {dish}:', 'new_dic': new_dic}
    return render(request, 'demo.html', context)


