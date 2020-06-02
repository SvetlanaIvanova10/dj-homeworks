from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product)
    list_reviews = request.session['reviewed_products']
    if request.method == 'GET':
            is_review_exist = False
            form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(text=form.cleaned_data['text'], product=product)
            review.save()
            request.session.modified = True
            if pk not in list_reviews:
                list_reviews.append(pk)
            is_review_exist = True
            form = None

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
