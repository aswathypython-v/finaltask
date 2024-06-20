from django.urls import path
from . import views
from .views import logout_view, login_view
from .views import home_view




urlpatterns = [

    path('', home_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
