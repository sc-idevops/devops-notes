# users/urls.py
from django.urls import path
from .views import home, SignUp, think, like, delete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name = "home"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("think", think, name="think"),
    path("like", like, name="like"),
    path("delete", delete, name="delete"),

]
urlpatterns += staticfiles_urlpatterns()