from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ProductCreationForm
from django.views.decorators.csrf import csrf_exempt


def product_detail_view(request):
    context = {
        'title': 'product detail page'
    }
    return render(request, 'products/detail.html', context)


# @csrf_exempt
def Product_create_view(request):
    if request.method == 'GET':
        context = {
            'title': 'Create Form',
            'form': ProductCreationForm
        }
        return render(request, 'products/product_create.html', context)
    elif request.method == 'POST':
        # product_name = request.POST.get('name')
        # seller = request.POST.get('seller')
        # price = request.POST.get('price')
        # Product.objects.create(name=product_name, seller=seller, price=price)
        form = ProductCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            product = form.save()
            return HttpResponse('Product has been Created Successfully!', status=201)
        else:
            return HttpResponse('Product Creation Failed!', status=400)
