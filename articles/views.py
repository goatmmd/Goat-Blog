from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, FormView
from django.utils.translation import gettext_lazy as _
from articles.forms import AddPostForm, AddCommentForm
from articles.models import Post, Category


def my_view(request):
    posts = Post.objects.all()

    return render(request, 'ablog/postlist.html', context={'posts': posts})


class PostDetailView(DetailView, FormView):
    model = Post
    template_name = 'ablog/post_detail.html'
    context_object_name = 'object'
    form_class = AddCommentForm

    def get_success_url(self):
        success_url = self.request.POST.get('url')
        return success_url

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.post_id = self.request.POST.get('post_id')
        instance.save()
        return super().form_valid(form)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('comments').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = getattr(context['object'], 'likes')
        context['likes'] = [li for li in likes.all()]
        context['form'] = AddCommentForm()

        return context


class AddPostView(LoginRequiredMixin, FormView):
    form_class = AddPostForm
    template_name = 'ablog/add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class CategoryPost(View):

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        posts = Post.objects.filter(category=category)
        return render(request, 'ablog/category_posts.html', context={'posts': posts, 'category': category})


class LikeView(View):

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.likes.add(request.user)
        return redirect(reverse('post-detail', args=[pk]))


class UnLikeView(View):

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.likes.remove(request.user)
        return redirect(reverse('post-detail', args=[pk]))


def words_view(request):
    sentence = _('Welcome to my site')
    return HttpResponse(sentence)
