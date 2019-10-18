from django.urls import path

from . import views

urlpatterns = [
    # airport urls
    path('', views.airport_index, name='airport_index'),
    path('new', views.airport_create, name='airport_create'),
    path('<int:airport_id>/delete', views.airport_delete, name='airport_delete'),
    path('<int:airport_id>', views.airport_update, name='airport_update'),

    # airline urls
    path('airline/', views.airline_index, name='airline_index'),
    path('airline/new', views.airline_create, name='airline_create'),
    path('airline/<int:airline_id>/delete', views.airline_delete, name='airline_delete'),
    path('airline/<int:airline_id>', views.airline_update, name='airline_update'),

    # plane urls
    path('plane/', views.plane_index, name='plane_index'),
    path('plane/new', views.plane_create, name='plane_create'),
    path('plane/<int:plane_id>/delete', views.plane_delete, name='plane_delete'),
    path('plane/<int:plane_id>', views.plane_update, name='plane_update'),

    # gate urls
    path('gate/', views.gate_index, name='gate_index'),
    path('gate/new', views.gate_create, name='gate_create'),
    path('gate/<int:gate_id>/delete', views.gate_delete, name='gate_delete'),
    path('gate/<int:gate_id>', views.gate_update, name='gate_update'),

    # runway urls
    path('runway/', views.runway_index, name='runway_index'),
    path('runway/new', views.runway_create, name='runway_create'),
    path('runway/<int:runway_id>/delete', views.runway_delete, name='runway_delete'),
    path('runway/<int:runway_id>', views.runway_update, name='runway_update'),
]