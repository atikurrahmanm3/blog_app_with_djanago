from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.home),
    path('about/', include('about.urls')),

]
