from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import user_passes_test

def render_with_context(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def storage_location(function, storage=None):
    """
    Decorator (wrapper) for automatic storage location specification
    """
    if storage is None:
        from django.core.files.storage import default_storage as storage

    actual_decorator = user_passes_test(
        lambda u: storage.specify_location(u.username)
    )
    return actual_decorator(function)
