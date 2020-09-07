from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),

    path('citymunicipality/', views.citymunicipality, name = "citymun"),
    path('barangay/', views.barangay, name = "barangay"),

    path('barangay_listing/', views.listingbarangay, name = "listingbarangay"),
    path('citymun_listing/', views.listingcitymun, name = "listingcitymun"),

    path('update_barangay/<str:pk>/', views.update_Barangay, name="update_barangay"),
    path('delete_barangay/<str:pk>/', views.delete_Barangay, name ="delete_barangay")

]