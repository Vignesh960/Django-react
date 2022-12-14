
from django.urls import path,include
from rest_framework.authtoken import views
from .views import home
urlpatterns = [
    path('',home,name='api.home'),#here name=app.view/function name==>api.home
    
]