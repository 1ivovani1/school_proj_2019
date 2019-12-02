from django.urls import path
from CIP_students.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('register',register),
    path('add_proj',add_proj),
    path('page',userPage),
    path('login',login_page),
    path('logout',logout_page),
    path('', mainPage),
    path('verification',register_code_enter),
] + static('media/', document_root = 'media/')
