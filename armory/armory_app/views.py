from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from armory_app.models import Post
from django.views.generic import View
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'armory_app/index.html')

def includes(request, req_file='about.html'):
    include = 'armory_app/includes/%s' % req_file
    template = include
    return render(request, include)

def post_list(request):
    posts = Post.objects.order_by('-post_date')[:5]
    return render(request, 'armory_app/post_list.html', {'posts': posts})

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'armory_app/detail.html', {'post': post})

def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        submission_text = post.comment_set.get(pk=request.POST['com_text'])
        submission_author = post.comment_set.get(pk=request.POST['com_author'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'armory_app/detail.html', {
            'comment': comment,
            'error_message': "You didn't submit a comment.",
        })
    else:
        return HttpResponse("You're commenting on post %s." % post_id)