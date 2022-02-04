from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('editar_tarea/<int:pk>/', views.editar_tarea, name="editar_tarea"),
    path('eliminar_tarea/<int:pk>/', views.eliminar_tarea, name="eliminar_tarea"),
    path('registro/', views.registro, name='registro'),
]
