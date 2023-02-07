from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgot_password/', views.forgot_password, name ='forgotPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name ='resetPassword'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name ='change_password'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('order_detail/<int:order_id>/',views.order_detail,name='order_detail'),
    path('user_cancel_order/<int:order_number>/', views.user_cancel_order, name='user_cancel_order'),
    path('user_manage_order/', views.user_manage_order, name='user_manage_order'),

]
