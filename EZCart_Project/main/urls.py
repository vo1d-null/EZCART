from django.urls import path
from django.conf.urls.static import static 
from ecommerce import settings 
from . import views 


urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about, name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)