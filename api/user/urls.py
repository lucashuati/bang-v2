from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', views.UserView, basename='user')

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
] + router.urls
