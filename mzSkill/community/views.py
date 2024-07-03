from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {"posts":posts})

def create_post(request): # create
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
    
def create_comment(request, id): # 댓글작성
    form = CommentForm(request.POST)
    if form.is_valid(): 
        unfinished_form = form.save(commit=False)
        unfinished_form.linked_post = Post.objects.get(id=id)   
        unfinished_form.author = request.user
        unfinished_form.save() 
    return redirect('community:post_detail', id)
    
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    profile = None
    try:
        profile = Learner.objects.get(user_id=post.author.id)
    except Learner.DoesNotExist:
        try:
            profile = Teacher.objects.get(user_id=post.author.id)
        except Teacher.DoesNotExist:
            profile = None
    except MultipleObjectsReturned:
        profile = None  # 또는 적절한 처리를 해주세요.

    comment_form = CommentForm()
    got_comments = Comment.objects.filter(linked_post=post).order_by('created_at')
    comments = []
    for comment in got_comments:
        try:
            com_author = Learner.objects.get(user_id=comment.author.id)
        except:
            com_author = Teacher.objects.get(user_id=comment.author.id)
        comments.append({'com_content': comment.content, 'com_nickname': com_author, 'author':comment.author, 'id': comment.id})
    context = {
        'post': post,  # id에 해당하는 post객체 하나
        'profile': profile,  # post객체 작성한 Learner혹은 Teacher객체 하나 
        'comment_form': comment_form,  # CommentForm()
        'comments': comments,  # com_content, com_nickname으로 이루어진 딕셔너리들의 리스트 
        'is_liked': request.user in post.liked_users.all(),
        'total_likes': post.liked_users.count(),
        'total_comments' : got_comments.count(), # 댓글 총 개수
    }
    return render(request, "post_detail.html", context)

# 게시글 삭제
def delete_post(request, id):
    post = get_object_or_404(Post, id = id)
    if request.user == post.author:
        post.delete()
    return redirect('community:community')

# 댓글 삭제
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.user == comment.author:
        linked_post_id = comment.linked_post.id
        comment.delete()
        return redirect('community:post_detail', id=linked_post_id)
    else:
        # 권한이 없는 경우 처리
        return redirect('community:post_detail', id=comment.linked_post.id)

# 좋아요 추가 기능/ 취소 기능
@login_required
def add_like(request, post_id):
    # post객체가 Post 모델을 받아옴으로서  템플릿에서는 {{post.title(나 content 등)}}을 사용가능한것
    post = get_object_or_404(Post, id = post_id)
    post.liked_users.add(request.user)
    return redirect('community:post_detail', id = post_id)

@login_required
def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.liked_users.remove(request.user)
    return redirect('community:post_detail', id = post_id)

# 게시글 수정
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        return redirect('community:post_detail', id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})
