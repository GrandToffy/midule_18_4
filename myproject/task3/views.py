from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        "Игровая приставка": "$299",
        "Игровой компьютер": "$1499",
        "Геймпад": "$59"
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')
