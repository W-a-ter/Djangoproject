from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDeleteView, CatalogCreateView, CatalogUpdateView, CatalogDetailView
from django.views.decorators.cache import cache_page
app_name = CatalogConfig.name


# urlpatterns = [
#     path('', home, name='home'),
#     path('contacts', contacts, name='contacts'),
#     path('catalog/<int:pk>/', product_detail, name='product'),
# ]

urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    #path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='product'),
    path('catalog/create', CatalogCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', CatalogUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', CatalogDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', cache_page(60)(CatalogDetailView.as_view()), name='product_cache')
]
