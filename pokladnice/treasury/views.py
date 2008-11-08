from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage as storage
from django.views.generic.simple import direct_to_template

from treasury.forms import FileUploadForm
from treasury.models import FileUpload

@login_required
def index(request):
    data = {}
    for func in [upload, space_meter, uploaded_files]:
        data.update(func(request))
    return direct_to_template(request, 'index.html', data)

#@login_required
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileUploadForm(request.user)

    #return direct_to_template(request, 'upload.html', {'form': form})
    return {'form': form}

def space_meter(request):
    size = {}; percent = {}; res = {'space': {}}

    size['total'] = storage.limit
    size['used'] = storage.get_used_space(user=request.user)
    size['free'] = size['total'] - size['used']
    res['space']['concrete'] = size

    # Filling result with percents
    def make_percent(num1, num2):
        return int((float(num1) / float(num2)) * 100)

    percent['free'] = make_percent(size['free'], size['total'])
    percent['used'] = 100 - percent['free']
    res['space']['percent'] = percent

    return res

def uploaded_files(request):
    """List user's uploaded files."""
    return {'uploaded_files': FileUpload.objects.filter(user=request.user)}

@login_required
def profile(request, username):
    return direct_to_template(request, 'profile.html', {'username': username})

@login_required
def delete(request, id):
    FileUpload.objects.filter(id=id).delete()
    return direct_to_template(request, 'deleted.html')
