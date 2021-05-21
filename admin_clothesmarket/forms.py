from django import forms
from main_clothesmarket.models import Category, Kind, Product


# creation form of category

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=16,
                            widget=forms.TextInput(attrs={'placeholder': 'Название', 'required': 'required'}))

    category_order = forms.IntegerField(
                            widget=forms.TextInput(attrs={'placeholder': 'Порядок категории в меню',
                                                          'required': 'required'}))
    photo = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Category
        fields = ('title', 'category_order', 'photo', 'is_visible')


# creation form of kinds

class KindForm(forms.ModelForm):
    title = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'Название', 'required': 'required'}))

    kind_order = forms.IntegerField(
                            widget=forms.TextInput(attrs={'placeholder': 'Порядок категории в базе',
                                                          'required': 'required'}))
    photo = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)
    des = forms.CharField(max_length=150,
                          widget=forms.TextInput(attrs={'placeholder': 'Описание',
                                                        'required': 'required'}))

    category = Category

    class Meta:
        model = Kind
        fields = ('title', 'kind_order', 'photo', 'is_visible', 'des', 'category')


# creation form of category


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'Название', 'required': 'required'}))
    manufactura = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={'placeholder': 'Бренд', 'required': 'required'}))

    product_order = forms.IntegerField(
                            widget=forms.TextInput(attrs={'placeholder': 'Порядок категории в базе',
                                                          'required': 'required'}))
    photo = forms.ImageField(widget=forms.FileInput())
    subphoto1 = forms.ImageField(widget=forms.FileInput())
    subphoto2 = forms.ImageField(widget=forms.FileInput())
    subphoto3 = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2,
                               widget=forms.TextInput(attrs={'placeholder': 'Цена', 'required': 'required'}))
    des = forms.CharField(max_length=150,
                          widget=forms.TextInput(attrs={'placeholder': 'Описание',
                                                        'required': 'required'}))
    category = Kind
    size = forms.CharField(max_length=30,
                          widget=forms.TextInput(attrs={'placeholder': 'Размер',
                                                        'required': 'required'}))

    available = forms.BooleanField(initial=True, required=False)
    slug = forms.SlugField(max_length=200)

    class Meta:
        model = Product
        fields = ('title', 'manufactura', 'product_order', 'photo', 'subphoto1', 'subphoto2', 'subphoto3',
                  'is_visible', 'price', 'des', 'category', 'size', 'available', 'slug')