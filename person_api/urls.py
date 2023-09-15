from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.person_list, name='person_list'),
    path('people/<int:pk>/', views.person_detail, name='person_detail'),
    # Add URL patterns for create and update views as needed
]
