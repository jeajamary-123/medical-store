from django.contrib import admin
from django.urls import path
from medicine_store import views
from medicine_store.views import retrieve_items
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('create/',views.product_create,name='create'),

    path('retrieved',views.retrieve_items,name='retrieve'),
    path('update/<int:id>/',views.product_update,name='updateproduct'),
    path('delete/<int:id>',views.product_delete,name='deleteproduct'),
    path('search/', views.search_medicine, name='search_medicine'),
    path('api/',include('api.urls')),
    

     ]


