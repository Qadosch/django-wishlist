from django.http import HttpResponse
from django.template import loader

from .. import models

__all__ = [
    "wishlist_view"
]

def wishlist_view(request):
    # TODO: Needs refactoring, only temporary
    if request.method == 'POST':
        wish_id = request.POST['wish_id']
        ammount = request.POST['ammount']
        count = request.POST['count']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        comment = request.POST['comment']

        models.Gift.objects.create(
            wish_id = wish_id,
            ammount = ammount,
            count = count,
            name = name,
            email = email,
            address = address,
            phone = phone,
            comment = comment,
        )

    context = {"collection": models.Collection.objects.first()}
    template = loader.get_template('wishlist.html')
    return HttpResponse(template.render(context))
