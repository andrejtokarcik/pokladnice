from lib import render_with_context
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render_with_context(request, 'home.html')

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})
