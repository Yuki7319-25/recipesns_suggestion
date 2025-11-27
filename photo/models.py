from django.conf import settings
from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    """投稿する写真のカテゴリ"""
    title = models.CharField(verbose_name='カテゴリ', max_length=20)

    def __str__(self):
        return self.title


class PhotoPost(models.Model):
    """投稿された写真データ"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    title = models.CharField(verbose_name='タイトル', max_length=200)
    comment = models.TextField(verbose_name='コメント')
    recipe = models.TextField(verbose_name='レシピ', blank=True, null=True)  # 追加

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos'
    )
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',
        blank=True,
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def total_likes(self):
        """この投稿のいいね数を返す"""
        return self.favorite_set.count()


class Favorite(models.Model):
    """お気に入り管理"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ForeignKey(PhotoPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'photo')  # 同じ投稿を複数回お気に入りできない

    def __str__(self):
        return f"{self.user} -> {self.photo}"
