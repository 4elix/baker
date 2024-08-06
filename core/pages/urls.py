from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_path'),
    path('our team/', views.team_view, name='team_path'),
    path('products/', views.ListProductPages.as_view(), name='product_list_path'),
    path('products/categories/<int:cat_id>/', views.ShowProductByCategoryId.as_view(), name='show_category_path')
]
