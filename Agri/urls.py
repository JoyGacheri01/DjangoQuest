
from django.urls import path
from . import views

app_name = 'Agri'
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('blog/', views.blog, name="blog")
]
