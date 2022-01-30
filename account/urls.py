from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import dashboard, register, edit, user_list, user_detail, user_follow

# app_name = 'account'
urlpatterns = [
# post views
# path('login/', views.user_login, name='login'),
path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('', dashboard, name='dashboard'),
path('password_change/',PasswordChangeView.as_view(),name='password_change'),
path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('register/', register, name='register'),
path('edit/', edit, name='edit'),
path('users/follow/', user_follow, name='user_follow'),
path('users/', user_list, name='user_list'),
path('users/<username>/',user_detail, name='user_detail'),
]