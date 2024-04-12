from django.urls import path

from core import views

urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('categoria/', views.CategoriaView.as_view(), name='categoria_list'),
    path('categoria/create/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', views.CategeriaUpdate.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', views.CategoriaDelete.as_view(), name='categoria_delete'),
    path('producto/', views.ProductoView.as_view(), name='producto_create'),
]
