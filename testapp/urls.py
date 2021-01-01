from django.urls import path
from . import views
urlpatterns = [
    path('sign/', views.signup_view, name='signup_view'),
    path('log/',views.login_view,name='login_view'),
    path('prof/',views.profile_view,name='profile'),
    path('logut/',views.logout_view,name='logout_view'),
    path('change/',views.passwrod_change,name='change'),
    path('change1/',views.passwrod_change1,name='change1'),
]