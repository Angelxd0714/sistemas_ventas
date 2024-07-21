from django.urls import path

from core import views

urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('categoria/', views.CategoriaView.as_view(), name='categoria_list'),
    path('categoria/create/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', views.CategeriaUpdate.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', views.CategoriaDelete.as_view(), name='categoria_delete'),
    path('producto/create', views.ProductoView.as_view(), name='producto_create'),
    path('producto/listar', views.ProductoListView.as_view(),name='producto_listar'),
    path('clientes/listar', views.ClientesListView.as_view(),name='clientes_listar'),
    path('clientes/create', views.CLientesCreate.as_view(), name='clientes_create'),
]
