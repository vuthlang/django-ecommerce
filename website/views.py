#from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def product_detail(request):
    return render(request, 'index_detail.html')


def cart(request):
    return render(request, 'cart.html')