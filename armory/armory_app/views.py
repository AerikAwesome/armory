from django.shortcuts import render
from django.http import Http404
from armory_app.models import Post

# Create your views here.
def index(request):
    return render(request, 'armory_app/index.html')

def blog(request, req=0):
    include = 'armory_app/blog/blog.html'
    start_of_range = int(req)
    end_of_range = start_of_range + 10
    latest_post_list = Post.objects.order_by('post_date')[start_of_range:end_of_range]
    context = {
               'latest_post_list': latest_post_list,
    }
    return render(request, include, context)

def includes(request, req_file='about.html'):
    include = 'armory_app/includes/%s' % req_file
    return render(request, include)

def blog_detail(request, req):
    try:
        post = Post.objects.get(pk=req)
    except Post.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'armory_app/blog/detail.html', {'post': post})


'''
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
'''