from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    """PhotoPostモデル用のフォーム"""
    class Meta:
        model = PhotoPost
        # 'recipe' を追加
        fields = ['category', 'title', 'comment', 'recipe', 'image1', 'image2']
