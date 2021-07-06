from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('<int:sno>', sno, name="sno"),
    path('search', search, name="search"),
    path('upload', upload, name="upload"),
   

    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
