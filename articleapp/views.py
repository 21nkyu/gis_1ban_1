from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from decorators import decorator


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    # success_url = reverse_lazy('accountapp:list')
    template_name = 'articleapp/cteate.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):   #detailview임에도 create처럼 뭔가를 만들 수 있다
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    #만드는 것도 업고 바로 템플릿
    template_name = 'articleapp/detail.html'
    #이제 path 설정 html만들기기


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    # 어떤값 설정 할건지 form을 받는다
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    #수정했을때 향하는 페이지
    # success_url = reverse_lazy('') #게시글 상세페이지로 //특정 계시글로 가기 위해서는 클래스 변수가 아니라 클래스를 하나 만들어야한다
    #템플릿 어떤것을 사용할 것이냐
    template_name = 'articleapp/update.html'
    #routing을 해준다 urls

    def get_success_url(self):                       #어떤특정 계시글로 가라
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})
    # kwargs는 딕셔너리


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list') #글을 지욱나면 갈곳이 없기 때문에
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'        #디테일 단일개체 타겟 아티클 여기서는 리스트름 담고 있는
    template_name = 'articleapp/list.html'     #로렌픽섬 리스트 그대사용 내용은 수정 할서임
    paginate_by = 20