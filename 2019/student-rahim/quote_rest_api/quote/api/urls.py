from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateQuote.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyQuote.as_view()),
    path('<int:quote_pk>/tags/', views.ListCreateTag.as_view()),
    path('<int:quote_pk>/tags/<int:pk>/', views.RetrieveUpdateDestroyTag.as_view()),

]