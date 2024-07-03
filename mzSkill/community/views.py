from django.shortcuts import render, redirect
from .forms import *


def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {"posts":posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): 
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('community:community')
    else:
        form = PostForm() 
        return render(request, 'create_post.html', {'form':form})
    
def create_comment(request, id):
    form = CommentForm(request.POST)
    if form.is_valid(): 
        unfinished_form = form.save(commit=False)
        unfinished_form.linked_post = Post.objects.get(id=id)   
        unfinished_form.author = request.user
        unfinished_form.save() 
    return redirect('community:post_detail', id)
    
def post_detail(request, id):
    post = Post.objects.get(id=id)

    profile = ''
    try:
        profile = Learner.objects.get(user_id = post.author.id)
    except:
        profile = Teacher.objects.get(user_id = post.author.id)

    comment_form = CommentForm()
    got_comments = Comment.objects.filter(linked_post=post).order_by('created_at')
    comments = []
    for comment in got_comments:
        try:
            com_author = Learner.objects.get(user_id = comment.author.id)
        except:
            com_author = Teacher.objects.get(user_id = comment.author.id)
        comments.append({'com_content':comment.content, 'com_nickname':com_author})

    context = {
        'post':post, # id에 해당하는 post객체 하나
        'profile':profile, # post객체 작성한 Learner혹은 Teacher객체 하나 
        'comment_form':comment_form, # CommentForm()
        'comments':comments # com_content, com_nickname으로 이루어진 딕셔너리들의 리스트 
    }
    return render(request, "post_detail.html", context)