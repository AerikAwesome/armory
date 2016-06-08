from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Post

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blog/detail.html', {'post': post})

def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        submission_text = post.comment_set.get(pk=request.POST['com_text'])
        submission_author = post.comment_set.get(pk=request.POST['com_author'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'comment': comment,
            'error_message': "You didn't submit a comment.",
        })
    else:


    return HttpResponse("You're commenting on post %s." % post_id)