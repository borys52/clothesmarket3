from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', list_of_messages, name='list_of_messages'),
    path('messages/update/<int:pk>/', update_message, name='update_message'),
    path('messages/updated_messages/', updated_messages, name='updated_messages'),
    path('cancel_update_message/<int:pk>/', cancel_update_message, name='cancel_update_message'),

    path('categories/', list_of_categories, name='list_of_categories'),
    path('categories/add/', CategoryAddView. as_view(), name='categories_add'),
    path('categories/delete/<int:pk>/', CategoryDeleteView. as_view(), name='categories_delete'),
    path('categories/update/<int:pk>/', CategoryUpdateView. as_view(), name='categories_update'),

    path('kinds/', list_of_kinds, name='list_of_kinds'),
    path('kinds/add/', KindAddView. as_view(), name='kinds_add'),
    path('kinds/delete/<int:pk>/', KindDeleteView. as_view(), name='kinds_delete'),
    path('kinds/update/<int:pk>/', KindUpdateView. as_view(), name='kinds_update'),

    path('list_of_products/', list_of_products, name='list_of_products'),
    path('list_of_products/add/', ProductAddView. as_view(), name='product_add'),
    path('list_of_products/delete/<int:pk>/', ProductDeleteView. as_view(), name='product_delete'),
    path('list_of_products/update/<int:pk>/', ProductUpdateView. as_view(), name='product_update'),
    ]
