from django.urls import path 
from medicamentos import views 

app_name = 'medicamentos'

urlpatterns = [
    path('medicamentos/crear/', views.CrearMedicamento.as_view(), name='crear_medicamento'),
    path('medicamentos/', views.ListadoMedicamentos.as_view(), name='listado_medicamentos'),
    path('medicamentos/<int:pk>/', views.VerMedicamentos.as_view(), name='ver_medicamentos'),
    path('medicamentos/<int:pk>/editar/', views.EditarMedicamentos.as_view(), name='editar_medicamentos'),
    path('medicamentos/<int:pk>/eliminar/', views.EliminarMedicamento.as_view(), name='eliminar_medicamento'),
    path('perfumes/crear/', views.CrearPerfumes.as_view(), name='crear_perfumes'),
    path('perfumes/', views.ListadoPerfumes.as_view(), name='listado_perfumes'),
    path('perfumes/<int:pk>/', views.VerPerfumes.as_view(), name='ver_perfumes'),
    path('perfumes/<int:pk>/editar/', views.EditarPerfumes.as_view(), name='editar_perfumes'),
    path('perfumes/<int:pk>/eliminar/', views.EliminarPerfume.as_view(), name='eliminar_perfume'),
]
