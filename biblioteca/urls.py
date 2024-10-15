from django.urls import path
from biblioteca import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('marcar-como-favorito', views.FavoritoView.as_view(), name='marcar_como_favorito')
]