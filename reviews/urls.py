from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='index'),
    path('consultar/<int:pk>', views.ReviewDetailView.as_view(), name='consultar'),
    path('modificar/<int:pk>', views.ReviewUpdateView.as_view(), name='modificar'),
    path('registrar', views.ReviewCreateView.as_view(), name='registrar'),
    path('registro_exitoso', views.ReviewSuccessView.as_view(), name='registro_exitoso'),
]