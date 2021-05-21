from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from main_clothesmarket.forms import Message
from main_clothesmarket.models import Category, Kind, Product
from order_clothesmarket.models import Order, OrderItem
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .forms import CategoryForm, KindForm, ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import GroupRequiredMixin

# Function for exist user in group


def is_member(user):
    return user.groups.filter(name='manager').exists() or \
           user.is_staff

# Function for access user to manage list of messages


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_messages(request):
    messages = Message.objects.filter(is_processed=False).order_by('pub_date')
    paginator = Paginator(messages, 2)
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    return render(request, 'messages.html', context={'messages': messages})

# Function for access user to manage list of messages (update)


@login_required(login_url='/login/')
@user_passes_test(is_member)
def update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/admin-panel/messages/')

# Function for access user to manage list of messages (view deleted messages)


@login_required(login_url='/login/')
@user_passes_test(is_member)
def updated_messages(request):
    messages = Message.objects.filter(is_processed=True)
    return render(request, 'updated_messages.html', context={'messages': messages})

# Function for access user to manage list of messages (cancel deleted messages)


@login_required(login_url='/login/')
@user_passes_test(is_member)
def cancel_update_message(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=False)
    return redirect('list_of_messages')

# Function for access user to manage list of categories


@login_required(login_url='/login/')
@user_passes_test(is_member)
def list_of_categories(request):
    items = Category.objects.all().order_by('category_order')
    return render(request, 'categories.html', context={'items': items})

# Class for access user to manage list of categories(add categoty in list)


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно создана!'

# Class for access user to manage list of categories(delete categoty)


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)


# Class for access user to manage list of categories(update categoty in list)


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Категория успешно изменена!'


# function for access user to manage list of kinds


login_required(login_url='/login/')
user_passes_test(is_member)


def list_of_kinds(request):
    items = Kind.objects.all().order_by('kind_order')
    return render(request, 'kinds.html', context={'items': items})

# Class for access user to manage list of kinds(add kind in list)


class KindAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Kind
    form_class = KindForm
    template_name = 'kind_add.html'
    success_url = reverse_lazy('list_of_kinds')
    success_message = 'Категория успешно создана!'


# Class for access user to manage list of kinds(delete kind in list)


class KindDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Kind
    success_url = reverse_lazy('list_of_kinds')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категория успешно удалена!')
        return self.post(request, *args, **kwargs)


# Class for access user to manage list of kinds(update kind in list)


class KindUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Kind
    form_class = KindForm
    template_name = 'kind_update.html'
    success_url = reverse_lazy('list_of_kind')
    success_message = 'Категория успешно изменена!'

# function for access user to manage list of products


login_required(login_url='/login/')
user_passes_test(is_member)


def list_of_products(request):
    items = Product.objects.all().order_by('product_order')
    return render(request, 'list_of_products.html', context={'items': items})

# Class for access user to manage list of products(add product in list)


class ProductAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'
    success_url = reverse_lazy('list_of_products')
    success_message = 'Продукт успешно создан!'


# Class for access user to manage list of products(delete product in list)


class ProductDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Product
    success_url = reverse_lazy('list_of_products')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Продукт успешно удален!')
        return self.post(request, *args, **kwargs)

# Class for access user to manage list of products(update product in list)


class ProductUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager', 'admin']
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('list_of_product')
    success_message = 'Продукт успешно изменен!'