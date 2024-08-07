from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sympy import Q
from .models import Message
from profiles.models import Teacher, Learner # profiles 폴더의 models 파일에서 임포트

# 티쳐 목록을 보여주는 뷰(여기서 이제 티쳐역시 러너가 보낸 메세지를 받아야함.)
@login_required
def room(request):
    user = request.user
    
    if hasattr(user, 'learner'):  # 유저가 러너인 경우
        teachers = Teacher.objects.all()
        return render(request, 'chat/room.html', {'teachers': teachers})
    
    else:  # 유저가 티쳐인 경우 (러너가 아닐 경우)
        learners = set()
        messages = Message.objects.filter(receiver=user)
        for message in messages:
            learners.add(message.sender)
        return render(request, 'chat/room.html', {'learners': learners})

# 채팅창 렌더링 함수(채팅 시작)
@login_required
def chat_view(request, username):
    user = request.user
    receiver_user = get_object_or_404(User, username=username)
    
    try:
        receiver_profile = Learner.objects.get(user=receiver_user)
    except Learner.DoesNotExist:
        receiver_profile = Teacher.objects.get(user=receiver_user)

    is_teacher = Teacher.objects.filter(user=user).exists()

    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=user, receiver=receiver_user, content=content)

    messages = Message.objects.filter(sender=user, receiver=receiver_user) | Message.objects.filter(sender=receiver_user, receiver=user)
    messages = messages.order_by('timestamp')
    
    return render(request, 'chat/chat.html', {'receiver': receiver_profile, 'messages': messages, 'is_teacher': is_teacher,})

@login_required
def out(request, username):
    user = request.user
    receiver_user = get_object_or_404(User, username=username)
    
    #대화방 나가기
    Message.objects.filter(sender = user, receiver = receiver_user).delete()
    Message.objects.filter(
        sender=receiver_user, receiver=user
    ).delete()

    return redirect('chat:room')

# https://codiving.kr/104
# https://chasingdreams.tistory.com/74

#검색 기능 뷰 추가
@login_required
def searchroom(request):
    search = request.GET.get('search','')
    teachers = Teacher.objects.filter(user__username__icontains=search) if search else []
    return render(request, 'chat/search_room.html', {
        'teachers' : teachers,
        'search' : search
    })