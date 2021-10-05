from django.shortcuts import render
from products.models import Product
from django.views import View


class home_cbv(View):
    def get(self, request):
        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price') or None
        sort = request.GET.get('sort') or None
        return render(request, 'home.html', )

    def delete(self, request):
        name = request.DELETE.get('name') or None
        if name:
            Product.objects.delete()


def home_view(request):
    if request.method == 'GET':
        min_price = request.GET.get('min_price', 0)
        max_price = request.GET.get('max_price') or None
        sort = request.GET.get('sort') or None
    elif request.method == 'DELETE':
        name = request.DELETE.get('name') or None
        if name:
            Product.objects.delete()
    products = Product.objects.all()
    if int(min_price):
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if sort:
        if sort in ('price', 'name', 'seller'):
            products = products.order_by(sort)
    context = {
        'title': 'Home',
        'objects': products,
        'min_price': min_price,
        'max_price': max_price
    }
    return render(request, 'home.html', context)


def gsearch_view(request):
    return render(request, 'gsearch.html', {})


def about_view(request):
    context = {
        'title': 'About Us',
    }

    # return HttpResponse(temp_html.format(request.user))
    return render(request, 'about.html', context)


def contact_view(request):
    context = {
        'title': 'Contact Us',
        'topics': ['c1', 'c2', 'c3']
    }

    # return HttpResponse(temp_html.format(request.user))
    return render(request, 'contact.html', context)
