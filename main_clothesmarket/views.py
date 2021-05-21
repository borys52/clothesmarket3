from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Kind, Product, Phone, Adress, OpeningHours, ShopInfo, AboutUs
from .forms import FormMessage
from cart_clothesmarket.cart import Cart

# Create your views here.

#  Function for display main page


def main_page_view(request):
    global categories
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        kinds = Kind.objects.filter(category=item.pk).filter(is_visible=True).order_by('kind_order')
        item.kinds = kinds
    promo = Kind.objects.filter(category__title='Акция')
    return render(request, 'index.html', context={
        'categories': categories,
        'promo': promo,

    })


# function for view objects of category 'Женщины'


def product_woman_view(request):
    product = Kind.objects.filter(category__title='Женщины')
    return render(request, 'products.html', context={
        'product': product,
        'categories': categories,

    })

# function for view objects of category 'Мужчины'


def product_man_view(request):
    product = Kind.objects.filter(category__title='Мужчины')
    return render(request, 'products.html', context={
        'product': product,
        'categories': categories,
    })

# function for view objects of category 'Сумки'


def product_bags_view(request):
    product = Kind.objects.filter(category__title='Сумки')
    return render(request, 'products.html', context={
        'product': product,
        'categories': categories,
    })


# function for display kinds of product


def categoryt_detail_view(request, pk):
    product = Kind.objects.filter(category=pk)
    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, 'products.html', context={
        'product': product,
        'categories': categories,
    })


# function for display products in kinds


def product_detail_view(request, pk):
    product = Product.objects.filter(category=pk)
    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    cart = Cart(request)
    return render(request, 'products_kind.html', context={
        'product': product,
        'cart': cart,
        'categories': categories,
    })

# function for display choosen product


def kind_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    cart = Cart(request)
    return render(request, 'product_detail.html', context={
        'product': product,
        'categories': categories,
        'cart': cart,
    })

# function for filter products bt id, slug, available


def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product_detail.html', context={
                  'product': product,
                  'cart': cart,
    })

# function for display contact information, and sending message


def contact_page_view(request):
    phone = Phone.objects.all()
    adress = Adress.objects.all()
    openinghours = OpeningHours.objects.all()
    shopinfo = ShopInfo.objects.all()

    if request.method == 'POST':

        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = FormMessage()
    return render(request, 'contact.html', context={
        'form': form,
        'categories': categories,
        'phone': phone[0],
        'adress': adress[0],
        'openinghours': openinghours[0],
        'shopinfo': shopinfo[0],


    })
#  fonction for filter by kinds


def get_products_queryset(request):
    product = Product.objects.filter(Q(category__in=request.GET.getlist("category_id")) | Q(manufactura=('Adidas')))
    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    # product = Product.objects.filter(manufactura='Adidas')
    return render(request, 'products_kind.html', context={
        'product': product,
        'categories': categories,
    })


# function for seach by title of product


def get_queryset(request):
    product = Product.objects.filter(title__icontains=request.GET.get("q"))
    return render(request, 'products_kind.html', context={
        'product': product,
        'categories': categories,
    })


#  function for display information about shop
def about_us_view(request):
    aboutus = AboutUs.objects.filter(is_visible=True)
    return render(request, 'about_us.html', context={
        'aboutus': aboutus[0],
    })