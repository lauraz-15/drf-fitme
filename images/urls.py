from django.urls import path
from images import views

urlpatterns = [
    path('images/', views.ImageList.as_view()),
    path('images/<int:pk>/', views.ImageDetail.as_view()),
]