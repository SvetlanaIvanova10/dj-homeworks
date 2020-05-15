from django.shortcuts import render
from phones.models import Phone
from phones.management.commands.import_phones import Command



def show_catalog(request):
    template = 'catalog.html'
    catalog = Command()
    catalog.handle()
    sort = request.GET.get('sort')
    if sort == 'name':
        data = Phone.objects.order_by("name")
    elif sort == 'min_price':
        data = Phone.objects.order_by("price")
    elif sort == 'max_price':
        data = Phone.objects.order_by("-price")
    else:
        data = Phone.objects.all()
    context = {
        "catalog": data
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data = Phone.objects.get(slug = slug)
    if data.lte_exists == 'True':
        lte_exists = 'Да'
    else:
        lte_exists = 'Нет'
    context = {'name': data.name,
               'image': data.image,
               'price': data.price,
               'release_date': data.release_date,
               'lte_exists': lte_exists}
    return render(request, template, context)
