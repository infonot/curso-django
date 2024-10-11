from django.urls import path
from perfiles import views

app_name = 'perfiles'

urlpatterns = [
    path('', views.PerfilUsuarioListView.as_view(), name='index'),
    path('registrar', views.PerfilUsuarioCreateView.as_view(), name='registrar'),
]