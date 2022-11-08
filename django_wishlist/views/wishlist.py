from django.core.mail import send_mail
from django.shortcuts import render
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
        ammount = request.POST.get('ammount', 0)
        count = request.POST.get('count', 0)
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        comment = request.POST['comment']

        wish = models.Wish.objects.get(pk=wish_id)

        gift = models.Gift.objects.create(
            wish = wish,
            ammount = ammount,
            count = count,
            name = name,
            email = email,
            address = address,
            phone = phone,
            comment = comment,
        )

        # Email to gifter
        send_mail(
            f'You gifted {gift.wish.title}',
            wish.email_template.format(**gift.values()),
            'tool@wishlist.4862.ch',
            [gift.email],
            fail_silently=False,
        )

        # Email to admin
        send_mail(
            f'You were gifted {gift.wish.title} from {gift.name}',
            '''
Hey, you were gifted
{wish.title}

ammount {ammount} / {wish.ammount}
count {count} / {wish.count}

from
{name}
{email}
{address}
{phone}

comment
{comment}

            '''.format(**gift.values()),
            'tool@wishlist.4862.ch',
            [wish.collection.user.email],
            fail_silently=False,
        )

    context = {"collection": models.Collection.objects.first()}
    # template = loader.get_template('wishlist.html')
    return render(request, "wishlist.html", context)
