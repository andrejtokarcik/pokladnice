from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage as storage

from lib import render_with_context
from forms import UploadFileForm
from models import UploadedFile

@login_required
def main(request):
    data = {}
    for func in [upload, space_meter]:
        data.update(func(request))
    return render_with_context(request, 'home.html', data)

#@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.cleaned_data['file']
            upl_file = UploadedFile(size=file_obj.size, user=request.user)
            upl_file.file.save(file_obj.name, file_obj)
            upl_file.save()
    else:
        form = UploadFileForm()

    #return render_with_context(request, 'upload.html', {'form': form})
    return {'form': form}

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})

def space_meter(request):
    size = {}; percent = {}; res = {'space': {}}

    size['total'] = storage.limit
    size['used'] = storage.get_used_space()
    size['free'] = size['total'] - size['used']

    # Filling result with percents
    def make_percent(num1, num2):
        return int((float(num1) / float(num2)) * 100)

    percent['free'] = make_percent(size['free'], size['total'])
    percent['used'] = 100 - percent['free']
    res['space']['percent'] = percent

    # Converting to megabytes (dirty?)
    for key in size.keys():
        size[key] = str(float(size[key]) / storage.megabyte)[:4]  # FIXME
        size[key] = ''.join([size[key], ' MB'])
    res['space']['concrete'] = size

    return res
