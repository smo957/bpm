from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name="activate"),
    path('login/', views.Login.as_view(), name="login")
]