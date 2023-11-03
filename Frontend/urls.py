from django.urls import path
from Frontend import views

urlpatterns = [

    path('homepage/', views.homepage, name="homepage"),
    path('productpage/', views.productpage, name="productpage"),
    path('singleproductpage/<int:proid>/', views.singleproductpage, name="singleproductpage"),
    path('filter_prdt_pg/<cat_name>/', views.filter_prdt_pg, name="filter_prdt_pg"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('savedata/', views.savedata, name="savedata"),
    path('registerpage/', views.registerpage, name="registerpage"),
    path('registersave/', views.registersave, name="registersave"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logout/', views.logout, name="logout"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('savecart/', views.savecart, name="savecart"),

    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),




]