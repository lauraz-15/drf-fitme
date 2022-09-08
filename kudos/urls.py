from django.urls import path
from kudos import views

urlpatterns = [
    path('kudos/', views.KudosList.as_view()),
]