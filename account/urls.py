from django.urls import path
from .views import account_login
app_name  = "account"
urlpatterns = [
    path("",account_login,name = "account_login")
]