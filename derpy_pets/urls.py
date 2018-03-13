from django.contrib import admin
from django.urls import path

from adoptions import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adoptions/<int:id>/', views.pet_detail, name='pet_detail'),
    path('new_pet', views.new_pet, name='new_pet'),
    path('adoptions/<int:id>/edit_pet/', views.edit_pet, name='edit_pet'),
]
