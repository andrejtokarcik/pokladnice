from django.http import HttpResponse, HttpResponseRedirect

def main(req):
    return HttpResponseRedirect('/prihlaseni')
