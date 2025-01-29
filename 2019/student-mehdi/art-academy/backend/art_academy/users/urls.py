
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # ---- user -----
    path('', views.UserListCreate.as_view(), name='user_list'), 
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'), 
    path('<str:username>/', views.UserDetail2.as_view(), name='username_detail'), 

    # ----- profile ----
    path('profiles/', views.ProfileList.as_view(), name='profile_list'), 
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'), 
    path('<int:user_pk>/profiles/', views.ProfileListCreate.as_view(), name='user_profile'), 
    path('<int:user_pk>/profiles/<int:pk>/', views.ProfileDetail.as_view(), name='user_profile_detail'),
    
    # ----- payment ----
    path('payments/', views.PaymentListCreate.as_view(), name='payment_list'), 
    path('payments/<int:pk>/', views.PaymentDetail.as_view(), name='payment_detail'), 
    path('<int:user_pk>/payments/', views.PaymentListCreate.as_view(), name='user_payment'), 
    path('<int:user_pk>/payments/<int:pk>/', views.PaymentDetail.as_view(), name='user_payment_detail'), 
]
