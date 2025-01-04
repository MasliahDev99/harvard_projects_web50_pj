from django.urls import path
from . import views

app_name = 'ganaderia'


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    #URLS HUB  
    path('hub/', views.hub, name='hub'),

    # URLS de dashboard
    path('hub/dashboard/', views.dashboard, name='dashboard'),
    path('hub/dashboard/ventas/', views.ventas, name='ventas'),
    path('hub/dashboard/ovejas/', views.ovejas, name='ovejas'),
    # URLS para ver el detalle de la oveja con id_oveja = id
    path('hub/dashboard/oveja/detalle/<int:id_oveja>/', views.ver_detalle, name='ver_detalle'),
    path('hub/dashboard/planteletas/', views.planteletas, name='planteletas'),
]
