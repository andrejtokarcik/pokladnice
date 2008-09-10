from django.conf import settings
from django.contrib.auth.decorators import login_required

from lib import render_with_context
from forms import UploadFileForm
from storage import TreasuryStorage

@login_required
def main(request):
    return render_with_context(request, 'home.html')

@login_required
def upload(request):
    errors = ''

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            storage = TreasuryStorage()
            storage.specify_location(request.user.username)
            storage.save(request.FILES['file'].name, request.FILES['file'])
    else:
        form = UploadFileForm()

    return render_with_context(request, 'upload.html',
            {'form': form, 'errors': errors})

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})
