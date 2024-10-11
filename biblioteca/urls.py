from django.urls import path
from biblioteca import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detalle_libro, name='detalle_libro')
]