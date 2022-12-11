from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from django.utils import timezone
from group.models import Group

# Create your views here.

class PostListView(ListView):

    # context_object_name = 'post_list'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')
    template_name = 'blog/all_posts.html'
    extra_context = {'title': 'Published Posts'}

class PostCreateViewNew(CreateView):

    model = Post
    fields = ('title','description')

    def form_valid(self, form: PostForm):
        form.instance.user = self.request.user
        group = Group.objects.filter(id=self.kwargs['pk']).first()
        form.instance.group = group
        return super().form_valid(form)
    extra_context = {'title': 'Write Your Blog'}

class PostDetailView(DetailView):

    model = Post
    extra_context = {'title': 'Post'}

class PostUpdateView(UpdateView):
    
    model = Post
    fields = ('title','description')
    # success_url = reverse_lazy('post:post_detail',pk=pk)
    extra_context = {'title': 'Update Your Blog'}


def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    gpk = post.group.id
    post.delete()
    return redirect('group:group_detail',pk=gpk)