from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('auth/',views.auth),
    path('signup/',views.signup),
    path('signup/create/',views.create),
    path('logout/',views.lgoout),
]
