from lib import render_with_context
from forms import UploadFileForm
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render_with_context(request, 'home.html')

@login_required
def upload(request):
    errors = ''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            from os import mkdir, walk
            from os.path import exists, getsize, join

            destination = join(settings.STORAGE_LOCATION,
                    request.user.username)
            if not exists(destination):
                mkdir(destination)

            def get_dir_size(directory):
                """Get size of directory contents"""
                dir_size = 0
                for path, dirs, files in walk(directory):
                    for file in files:
                        dir_size += getsize(join(path, file))
                    for dir in dirs:
                        dir_size += get_dir_size(join(path, dir))
                return dir_size

            if (get_dir_size(destination) + request.FILES['file'].size) > (settings.STORAGE_LIMIT * 1024 ** 2):
                errors = 'Limit dosiahnuty\n'
            else:
                destination = open(join(destination,
                    request.FILES['file'].name), 'wb+')

                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
    else:
        form = UploadFileForm()
    return render_with_context(request, 'upload.html',
            {'form': form, 'errors': errors})

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})
