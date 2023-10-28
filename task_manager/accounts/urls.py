from django.urls import path
from .views import loginuser,ownerprofile,logoutuser,signupview,change_passwordview,userProfile,otherprofile
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    path('login/',loginuser, name='login'),
    path('logout/',logoutuser,name='logout'),
    path('ownerprofile/',ownerprofile,name='ownerprofile'),
    path('userprofile/',userProfile,name='userprofile'),
    path('otherprofile/<str:username>/',otherprofile,name='otherprofile'),
    path('signup/',signupview,name='signup'),
    path('changepassword/',change_passwordview,name='changepassword'),

    path('reset/password/',PasswordResetView.as_view(template_name='accounts/reset_pass.html'),name='password_reset'),
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name='accounts/reset_pass_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='accounts/pass_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='accounts/pass_reset_complete.html'),name='password_reset_complete'),
    
]
