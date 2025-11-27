from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import PhotoPost, Favorite
from .forms import PhotoPostForm

# ---------------------
# トップページ
# ---------------------
class IndexView(ListView):
    model = PhotoPost
    template_name = 'photo/index.html'
    context_object_name = 'records'
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset().order_by('-posted_at')
        if self.request.user.is_authenticated:
            for record in qs:
                record.is_favorited = record.favorite_set.filter(user=self.request.user).exists()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider_images'] = [
            'photo/images/haru.png',
            'photo/images/natu.png',
            'photo/images/aki.png',
            'photo/images/huyu.png',
        ]
        return context


# ---------------------
# 投稿
# ---------------------
class CreatePhotoView(LoginRequiredMixin, CreateView):
    form_class = PhotoPostForm
    template_name = 'photo/post_photo.html'
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'photo/post_success.html'


# ---------------------
# 投稿詳細・削除
# ---------------------
class PhotoDetailView(DetailView):
    model = PhotoPost
    template_name = 'photo/detail.html'

class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('photo:mypage')


# ---------------------
# マイページ
# ---------------------
class MypageView(LoginRequiredMixin, ListView):
    template_name = 'photo/mypage.html'
    paginate_by = 9
    login_url = '/accounts/login/'

    def get_queryset(self):
        return PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')


# ---------------------
# お気に入り一覧
# ---------------------
class FavoriteListView(LoginRequiredMixin, ListView):
    template_name = 'photo/favorites.html'
    context_object_name = 'favorites'
    paginate_by = 9
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by('-created_at')


# ---------------------
# Ajaxいいね
# ---------------------
@login_required
def favorite_toggle(request, pk):
    post = get_object_or_404(PhotoPost, pk=pk)
    favorite, created = Favorite.objects.get_or_create(user=request.user, photo=post)
    if not created:
        favorite.delete()
        is_favorited = False
    else:
        is_favorited = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'is_favorited': is_favorited,
            'total_likes': post.favorite_set.count(),
        })
    return redirect('photo:index')


# ---------------------
# 季節ページ
# ---------------------
def season_page(request, season):
    context = {
        'season': season
    }
    return render(request, 'photo/season_page.html', context)


# ---------------------
# 月ページ
# ---------------------
def month_page(request, month):
    return render(request, 'photo/month.html', {'month': month})


# ---------------------
# 会話ページ（これが必要！）
# ---------------------
def conversation_page(request, month):
    return render(request, 'photo/conversation.html', {'month': month})


# ---------------------
# カレンダー
# ---------------------
def calendar_view(request):
    months = [
        {'num': 1, 'season': '冬'},
        {'num': 2, 'season': '冬'},
        {'num': 3, 'season': '春'},
        {'num': 4, 'season': '春'},
        {'num': 5, 'season': '春'},
        {'num': 6, 'season': '夏'},
        {'num': 7, 'season': '夏'},
        {'num': 8, 'season': '夏'},
        {'num': 9, 'season': '秋'},
        {'num': 10, 'season': '秋'},
        {'num': 11, 'season': '秋'},
        {'num': 12, 'season': '冬'},
    ]
    return render(request, 'photo/calendar.html', {'months': months})
def conversation_page(request, month):
    # 月ごとの会話を辞書で用意
    conversations = {
        1: [
            ("店員さん", "いらっしゃいませ！1月のおすすめ料理はお雑煮です。"),
            ("お客さん", "それはどんな味ですか？"),
            ("店員さん", "優しいだしの味で、もちもちしています。")
        ],
        2: [
            ("店員さん", "いらっしゃいませ！2月のおすすめは恵方巻です。"),
            ("お客さん", "毎年食べます！"),
            ("店員さん", "ちなみにわたしはマグロの恵方巻が好きです。")
        ],
        3: [
            ("店員さん", "いらっしゃいませ！3月のおすすめはアサリのお味噌汁です。"),
            ("お客さん", "だしがきいて美味しいですね！"),
            ("店員さん", "温かく優しい味です。")
        ],
        4: [
            ("店員さん", "4月のおすすめは筍ご飯です。"),
            ("お客さん", "旬の味ですね！"),
            ("店員さん", "香り豊かでふっくら炊き上がっています。")
        ],
        5: [
            ("店員さん", "5月は柏餅がおすすめです。"),
            ("お客さん", "子どもの日ですね！"),
            ("店員さん", "甘さ控えめでお茶にぴったりです。")
        ],
        6: [
            ("店員さん", "6月のおすすめは梅干しです。"),
            ("お客さん", "夏バテ対策に体にいいですね。"),
            ("店員さん", "酸っぱさが食欲をそそりますよ。")
        ],
        7: [
            ("店員さん", "7月は冷やしそうめんがおすすめです。"),
            ("お客さん", "暑い日には最高ですね！"),
            ("店員さん", "つるっとのどごしが最高です。")
        ],
        8: [
            ("店員さん", "8月のおすすめはかき氷です。"),
            ("お客さん", "フルーツ味がいいなぁ。"),
            ("店員さん", "いちごやメロンなど色々美味しいのありますよ。")
        ],
        9: [
            ("店員さん", "9月は栗ご飯がおすすめです。"),
            ("お客さん", "秋の味覚ですね！"),
            ("店員さん", "ほくほくで甘みがあります。")
        ],
        10: [
            ("店員さん", "10月はきのこご飯です。"),
            ("お客さん", "香りが楽しみです。"),
            ("店員さん", "色んなきのこの旨味が出ています。")
        ],
        11: [
            ("店員さん", "11月は鍋料理がおすすめです。"),
            ("お客さん", "寒くなってきましたね。"),
            ("店員さん", "具沢山で体が温まります。カニ鍋たべてみたい")
        ],
        12: [
            ("店員さん", "12月はおせち料理がおすすめです。"),
            ("お客さん", "もう年越しですね！"),
            ("店員さん", "彩り豊かで一年の締めにぴったりです。")
        ],
    }

    # month が辞書にない場合のデフォルト
    conversation = conversations.get(month, [
        ("店員", f"{month}月のおすすめ料理はまだ準備中です。"),
        ("お客さん", "わかりました。")
    ])

    return render(request, 'photo/conversation.html', {
        'month': month,
        'conversation': conversation
    })
