from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.master, name='master'),
    path('<int:bouquet_id>/', views.detail, name='detail'),
]