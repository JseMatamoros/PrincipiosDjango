
from django.urls import path
from .views import IndexPageView, obtener_fecha, menu_view

urlpatterns = [
    path('', IndexPageView.as_view(), name ='index'),
    path('fecha/<str:name>/<int:foto>/', obtener_fecha, name ='fecha'),
    path('menu/', menu_view, name="menu"),
]

