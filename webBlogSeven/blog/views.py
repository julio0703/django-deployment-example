from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from blog.models import Post, Comment
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class AboutView(generic.TemplateView):
    template_name = 'about.html'

class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class DraftListView(LoginRequiredMixin, generic.ListView):
    login_url ='/login/'
    redirect_field_name = 'blog/post_list.html'
    context_object_name = 'post_draft_list'
    template_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

class PostDetailView(generic.DetailView):
    model = Post

class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm

class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


################################################################
################################################################
################################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)
