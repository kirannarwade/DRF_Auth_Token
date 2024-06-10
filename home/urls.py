from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view()),
    path('get-data/', views.GetData.as_view()),
]