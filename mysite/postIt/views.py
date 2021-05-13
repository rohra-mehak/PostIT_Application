from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm, UpdatePostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


# def Favourite(request, pk):
#     fav = False
#     if request.POST.get('fav') == '1':
#         post = get_object_or_404(Post, id=request.POST.get('post_id'))
#         print("im heree")
#         post.favourite = True
#         fav = False
#         return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]), {'fav': fav})
#
#     elif request.POST.get('fav') == '0':
#         post = get_object_or_404(Post, id=request.POST.get('post_id'))
#         'im here unfav'
#         post.favourite = False
#         fav = True
#         return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]), {'fav': fav})
#
#     return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]), {'fav': fav})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["liked"] = liked
        context["total_likes"] = total_likes

        return context


class MakeCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


# def MakeCommentView(response, pk):
#
#     if response.method == 'POST':
#         commentForm = CommentForm()
#         if commentForm.is_valid():
#             commentForm.save()
#             return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
#     else :
#         commentForm = CommentForm()
#     return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]), {"form": commentForm})


class MakePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'make_post.html'
    # fields = ('title', 'author', 'category', 'content', 'photo')


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'cat_posts': category_posts})


def FavouritesView(request):
    fav_posts = []
    results = Post.objects.all()
    for post in results:
        if post.likes.filter(id=request.user.id).exists():
            fav_posts.append(post)
    return render(request, 'favourites.html', {'fav_posts': fav_posts})


def SearchResultsView(request):
    query = request.GET.get('q')
    print(query)
    search_posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) |
        Q(category__icontains=query)
    )
    print(search_posts)
    return render(request, 'search_results.html', {'search_posts': search_posts})


def myPostsView(request):
    my_post_list = Post.objects.filter(author=request.user)
    print(my_post_list)
    return render(request, 'my_posts.html', {'my_post_list': my_post_list})


def delete_my_post(request, pk):
    post_to_delete = Post.objects.get(id=request.POST.get('post_id'))
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('my_posts'))


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = UpdatePostForm
        # initial={
        #     'title' : Post.title,
        #     'category': Post.category ,
        #     'photo' : Post.photo,
        #     'content' : Post.content
        # }

    template_name = 'update_post.html'
    #
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('my_posts')

    # def get_absolute_url(self):
    #     return reverse('my_posts')