from django.shortcuts import render

def home(request):
    return render(request, 'fourth_task/home.html')

def shop(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')
