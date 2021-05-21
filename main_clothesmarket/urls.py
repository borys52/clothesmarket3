from django.urls import path
from main_clothesmarket import views

from .views import *

app_name = 'main_clothesmarket'

urlpatterns = [
    path('', main_page_view, name='main_page_view'),

    path('filter/', get_products_queryset, name='product_filtered_view'),
    path('search/', get_queryset, name='search'),

    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),


    path('productsman/', product_woman_view, name='product_woman_view'),
    path('productsman/<int:pk>', product_detail_view, name='product_detail_view'),


    path('category_detail_view/<int:pk>', categoryt_detail_view, name='categoryt_detail_view'),

    path('kind_detail_view/<int:pk>', kind_detail_view, name='kind_detail_view'),

    path('productsman/', product_man_view, name='product_man_view'),
    path('productsman/<int:pk>', product_detail_view, name='product_detail_view'),
    path('productsman/', product_bags_view, name='product_bags_view'),
    path('productsman/<int:pk>', product_detail_view, name='product_detail_view'),


    path('contact.html', contact_page_view, name='contact_page_view'),
    path('aboutus/', about_us_view, name='about_us_view',)

]
