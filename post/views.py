from django.shortcuts import render,reverse, get_object_or_404
from post.models import Post
from post.forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse,Http404

# Create your views here.
def home_feed(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts": posts}
    return render(request, "home_feed.html", context)

def add_post(request):
    # form = TestForm(request.POST or None)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # context = {"form": form}
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form": form}
    return render (request, "add_post.html", context)   

def edit_post(request, post_id):
    # try:
    #     po = Post.object.get(id=post_id)
    # except Post.DoesNotExit:
    #     raise Http404("page not find")
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("post:home"))
    context = {"form": form}
    return render(request, "edit_post.html", context)