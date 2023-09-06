from django.shortcuts import render,get_object_or_404
from product.models import Product,Category,Review
from .forms import ReviewForm
from django.shortcuts import redirect,render
# Create your views here.
def home(request,category_slug=None):
    category = None
    cloth = None
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
        cloth = Product.objects.filter(category= category)
    else:
         cloth = Product.objects.all()
    
    searchItem = request.GET.get('inputfield')
    # if searchItem:
    #     cloth = Product.objects.filter(slug__icontains=searchItem)
    # else:
    #     cloth = Product.objects.all()
   
    category = Category.objects.all()
    return render(request,'product.html',{'cloth':cloth,'category':category})

def details(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    reviews = Review.objects.filter(product=product)
    average_rating = product.average_rating
    total_ratings = product.total_ratings
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            Product.update_average_rating()  
            return redirect('detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'details.html', {'product': product, 'reviews': reviews, 'average_rating': average_rating, 'total_ratings': total_ratings, 'form': form})




def create_review(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('details', product_id=product.id)

    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'product': product})

def filter(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', int('inf'))

    
    filtered_products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'filtered_cards': filtered_products,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'filter.html', context)