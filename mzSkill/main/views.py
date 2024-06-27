from django.shortcuts import render
# account에서 로그인 되어 있다는 전제하에
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render(request, 'main/main.html')
