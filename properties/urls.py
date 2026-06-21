from django.urls import path
from properties import views

urlpatterns = [
    path('<int:id>',views.property_detail,name="property_details"),
    path('dashboard',views.dashboard_details,name="dashboard"),
    path('add_property',views.add_new_property,name="add_property"),
    path('edit/<int:id>',views.propertyEdit,name='edit_property'),
    path("buy/<int:id>",views.buy,name='buy')
]