from lib import render_with_context
from forms import UploadFileForm
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render_with_context(request, 'home.html')

@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            from os.path import join as path_join
            destination = open(path_join(settings.STORAGE_LOCATION,
                               request.FILES['file'].name), 'wb+')

            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)
    else:
        form = UploadFileForm()
    return render_with_context(request, 'upload.html', {'form': form})

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})
