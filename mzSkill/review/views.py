from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Teacher
from .models import Review
from .forms import ReviewForm

# 리뷰 보여주기(matching/mzteacher_profile.html)
def show_review(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    reviews = Review.objects.filter(teacher=teacher).order_by('-id')
    return render(request, 'list.html', {"reviews":reviews, 'teacher':teacher})

# 리뷰 작성
@login_required
def write_review(request, teacher_username):
    teacher = get_object_or_404(Teacher, user__username=teacher_username)

    # 현재 사용자가 이미 이 티쳐에 대한 리뷰를 작성했는지 여부
    try:
        review = Review.objects.get(teacher=teacher, learner=request.user)
    except Review.DoesNotExist:
        review = None

    if request.method == 'POST':
        if review:
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.teacher = teacher
            review.learner = request.user
            review.save()
            return redirect('chat:chat_view', username=teacher_username)
    else:
        if review:
            form = ReviewForm(instance=review)  # 기존 리뷰 수정
        else:
            form = ReviewForm()  # 새로운 리뷰 작성

    return render(request, 'write_review.html', {'form': form, 'teacher': teacher})


# 리뷰 조회
@login_required
def teacher_reviews(request, teacher_username):
    teacher = get_object_or_404(Teacher, user__username = teacher_username)
    reviews = teacher.reviews.all()
    return render(request, 'review/teacher_reviews.html', {'teacher': teacher, 'reviews': reviews})


