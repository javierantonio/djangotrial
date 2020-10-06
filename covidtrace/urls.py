from django.contrib import admin
from django.urls import path, include
from . import controllers

urlpatterns = [
    path('', controllers.home, name ="home"),

    path('register/', controllers.registerUser, name ="register"),
    path('login/', controllers.loginuser, name ="login"),
    path('logout/', controllers.logoutuser, name ="logout"),

    path('citymunicipality/', controllers.citymunicipality, name ="citymun"),
    path('barangay/', controllers.barangay, name ="barangay"),

    path('barangay_listing/', controllers.listingbarangay, name ="listingbarangay"),
    path('citymun_listing/', controllers.listingcitymun, name ="listingcitymun"),

    path('update_barangay/<str:pk>/', controllers.update_Barangay, name="update_barangay"),
    path('delete_barangay/<str:pk>/', controllers.delete_Barangay, name ="delete_barangay"),

    path('update_citymun/<str:pk>/', controllers.update_Citymun, name="update_citymun"),
    path('delete_citymun/<str:pk>/', controllers.delete_Citymun, name="delete_citymun"),

    path('map/', controllers.map, name="map"),
    path('mapy/', controllers.mapy, name="mapy"),

    path('create_establishment/', controllers.create_establishment, name="create_establishment"),

    path('create_visitor/', controllers.create_visitor, name="create_visitor"),

    path('create_system_user/', controllers.create_system_user, name="create_system_user"),

]