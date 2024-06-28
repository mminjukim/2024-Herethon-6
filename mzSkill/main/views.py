from django.shortcuts import render
# account에서 로그인 되어 있다는 전제하에
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

@login_required
def main(request):
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request, 'main/main.html', {'profile':profile})
