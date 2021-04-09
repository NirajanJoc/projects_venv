from django.urls import path
from useraccounts.views import signup_view, UserLoginView, send_conform_email
from django.contrib.auth.views import LogoutView

app_name='user'
urlpatterns=[
    path('', UserLoginView.as_view(), name='login'),
    path('register/', signup_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('send-mail', send_conform_email, name='send_email')
]