from django.http import HttpResponse
from django.template import loader

from .. import models

__all__ = [
    "wishlist_view"
]

def wishlist_view(request):
  context = {"collection": models.Collection.objects.first()}
  template = loader.get_template('wishlist.html')
  return HttpResponse(template.render(context))
