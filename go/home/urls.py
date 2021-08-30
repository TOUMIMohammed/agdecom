from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('author/', views.author, name='author'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login, name='login'),
]