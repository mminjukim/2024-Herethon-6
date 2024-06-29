from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

# 채팅창 렌더링
@login_required
def chat_view(request, username):
    user = request.user
    receiver = User.objects.get(username=username)
    messages = Message.objects.filter(sender=user, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})

# 채팅장 목록 보여주기
def room(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/room.html', {'users': users})
