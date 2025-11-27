from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # カレンダーページ
    path('calendar/', views.calendar_view, name='calendar'),

    # 月ページ
    path('month/<int:month>/', views.month_page, name='month_page'),

    # 会話ページ ←★重要★
    path('conversation/<int:month>/', views.conversation_page, name='conversation'),

    # 投稿関連
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('photo-detail/<int:pk>/', views.PhotoDetailView.as_view(), name='detail'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),

    # マイページ
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('favorites/', views.FavoriteListView.as_view(), name='favorites'),

    # いいね
    path('favorite/<int:pk>/toggle/', views.favorite_toggle, name='favorite_toggle'),
]
