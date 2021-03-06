"""clothesmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from clothesmarket import settings
from account_clothesmarket.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cart_clothesmarket/', include('cart_clothesmarket.urls', namespace='cart_clothesmarket')),
    path('order_clothesmarket/', include('order_clothesmarket.urls', namespace='order_clothesmarket')),
    path('', include('main_clothesmarket.urls', namespace='main_shop')),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-panel/', include('admin_clothesmarket.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
