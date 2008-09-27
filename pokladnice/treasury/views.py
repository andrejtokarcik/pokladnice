from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage as storage

from lib import render_with_context, storage_location
from forms import UploadFileForm

@login_required
def main(request):
    data = {}
    for func in [upload, space_meter]:
        data.update(func(request))
    return render_with_context(request, 'home.html', data)

#@login_required
@storage_location
def upload(request):
    sent = (request.method == 'POST')
    if sent:
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            storage.save(request.FILES['file'].name, request.FILES['file'])
    else:
        form = UploadFileForm()

    #return render_with_context(request, 'upload.html', {'form': form})
    return {'form': form, 'sent': sent}

@login_required
def profile(request, username):
    return render_with_context(request, 'profile.html', {'username': username})

@storage_location
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
