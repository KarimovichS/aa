
from django.urls import path, re_path, register_converter
from . import views
from . import canverters


register_converter(canverters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/',views.show_category,name='category'),

]

