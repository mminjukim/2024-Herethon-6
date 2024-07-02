from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from profiles.models import Teacher, Learner # profiles 폴더의 models 파일에서 임포트

# 티쳐 목록을 보여주는 뷰(여기서 이제 티쳐역시 러너가 보낸 메세지를 받아야함.)
def room(request):
    user = request.user
    # 유저가 러너인 경우
    if hasattr(user, 'learner'): # 유저가 러너인 경우
        teachers = Teacher.objects.all()
        return render(request, 'chat/room.html', {'teachers': teachers})
    elif hasattr(user, 'teacher'): # 유저가 티쳐인 경우
        learners = set()
        messages = Message.objects.filter(receiver=user)
        for message in messages:
            learners.add(message.sender)
        return render(request, 'chat/room.html', {'learners': learners})
    else:
        return render(request, 'chat/error.html', {'error': '러너 또는 티쳐 계정이 아닙니다.'})

# 채팅창 렌더링 함수
@login_required
def chat_view(request, username):
    user = request.user
    receiver = get_object_or_404(User, username=username)
    if request.method == 'POST':
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=user, receiver=receiver, content=content)
    messages = Message.objects.filter(sender=user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})