from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import PostModel, Like
from .forms import PostModelForm
from django.views.generic import ListView, DeleteView

class TweetListView(ListView):
    model = PostModel
    template_name = 'feed.html'
    context_object_name = 'feed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostModelForm()

        user = self.request.user

        liked_posts = Like.objects.filter(user=user).values_list('post_id', flat=True)

        post_likes = {}
        feed = context['feed']
        for post in feed:
            post_likes[post.id] = post.like_set.count()

        context['liked_posts'] = liked_posts
        context['post_likes'] = post_likes

        return context


    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
        return self.get(request, *args, **kwargs)


class TweetDeleteView(DeleteView):
    model = PostModel
    template_name = 'post_delete.html'
    success_url = reverse_lazy('feed')

    def get_object(self):
        post_id = self.kwargs['post_id']
        return PostModel.objects.get(id=post_id)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    user = request.user

    like, created = Like.objects.get_or_create(post=post, user=user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    total_likes = post.like_set.count()

    return JsonResponse({'liked': liked, 'total_likes': total_likes})

