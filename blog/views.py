from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post
from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'created_at', 'is_published', 'views_counter']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'created_at', 'is_published', 'views_counter']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_detail')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

