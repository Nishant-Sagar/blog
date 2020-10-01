from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name= 'index'),
    path('post.html',views.post, name= 'post'),
    path('fashion',views.fashion, name= 'fashion'),
    path('gadgets',views.gadgets, name= 'gadgets'),
    path('lifestyle',views.lifestyle, name= 'lifestyle'),
    path('kitchen',views.kitchen, name= 'kitchen'),
    path('Mi_Cam',views.micam, name= 'Mi_Cam'),
    path('Nikon_D3500',views.nikon, name= 'nikon_D3500'),
]