from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # ユーザー登録
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    # ログイン・ログアウト
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    # 今日のメニューや welcome ページ
    path('today-menu/', views.today_menu_view, name='today_menu'),
    path('welcom_boad/', views.welcom_boad, name='welcom_boad'),
]
