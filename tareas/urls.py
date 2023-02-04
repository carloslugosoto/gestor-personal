from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='tareas'),
   path('view/<int:id>', views.view, name='tarea_view'),
   path('edit/<int:id>', views.edit, name='tarea_edit'),
   path('create/', views.create, name='tarea_create'),
   path('delete/<int:id>', views.delete, name='tarea_delete')
    
]