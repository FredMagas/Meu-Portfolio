from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download_curriculo/<int:curriculo_id>/', views.download_curriculo, name='download_curriculo'),
]