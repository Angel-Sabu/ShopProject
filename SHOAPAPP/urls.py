from django.urls import path
from SHOAPAPP import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('CategoryPage/', views.CategoryPage, name="CategoryPage"),
    path('savedata1/', views.savedata1, name="savedata1"),
    path('Categorydisplaypage/', views.Categorydisplaypage, name="Categorydisplaypage"),
    path('categoryeditpage/<int:dataid>/', views.categoryeditpage, name="categoryeditpage"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),

    path('Productspage/',views.Productspage, name="Productspage"),
    path('productsavedata/',views.productsavedata, name="productsavedata"),
    path('Productsdisplaypage/',views.Productsdisplaypage, name="Productsdisplaypage"),
    path('producteditpage/<int:dataid>/', views.producteditpage, name="producteditpage"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpages/',views.loginpages, name="loginpages"),
    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminlogout/',views.adminlogout, name="adminlogout"),
    path('contactus/',views.contactus, name="contactus"),


]