from django.urls import path
from regform.views import index, register, success

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register-page"),
    path("register/success/", success, name="success-page")
]
