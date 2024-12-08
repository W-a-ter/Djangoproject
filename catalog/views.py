from django.core.exceptions import PermissionDenied

from catalog.models import Product
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from catalog.forms import ProductForm, ProductModerForm
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.services import LoadProductCategory


# Create your views here


class CatalogListView(ListView):
    """Класс представления каталога товаров на главной странице"""
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CatalogDetailView(DetailView):
    """Класс представления полной информации о товаре, на отдельной странице"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_create")
    template_name = "catalog/catalog_form.html"
    context_object_name = "product_create"


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/catalog_form.html"

    def get_success_url(self):
        return reverse("catalog:product_update", args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModerForm
        raise PermissionDenied


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_create")


class ProductCategoryView(ListView):
    """Класс представления категории продуктов"""
    model = Product
    template_name = "catalog/product_category.html"
    context_object_name = 'product_category'

    def get_queryset(self):
        return LoadProductCategory.load_product_category(category_id=self.kwargs.get('pk'))


# def home(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'base_html.html', context)
#
#
# def contacts(request):
#     return render(request, 'contacts.html')
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail', context)
