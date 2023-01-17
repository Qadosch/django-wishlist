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
        amount = request.POST.get('amount', 0)
        count = request.POST.get('count', 0)
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        comment = request.POST['comment']

        wish = models.Wish.objects.get(pk=wish_id)

        gift = models.Gift.objects.create(
            wish = wish,
            amount = amount,
            count = count,
            name = name,
            email = email,
            address = address,
            phone = phone,
            comment = comment,
        )

        if wish.missing_count == 0 or wish.missing_amount == 0:
            wish.gifted = True
            wish.save()

        gift_context = {
            "count": count,
            "amount": amount,
            "name": name,
            "gift": wish.title,
            "comment": comment,
        }

        # Email to gifter
        send_mail(
           gift.wish.email_subject,
            wish.email_template.format(**gift_context),
            'wishlist@4862.ch',
            [gift.email],
            fail_silently=False,
        )

        # Email to admin
        send_mail(
            f'You were gifted {gift.wish.title} from {gift.name}',
            'Hey, you were gifted\n{title}\n\namount {amount} / {w_amount}\ncount {count} / {w_count}\n\nfrom\n{name}\n{email}\n{address}\n{phone}\n\ncomment\n{comment}\n\n'.format(title=wish.title,w_amount=wish.amount, w_count=wish.count, **gift.__dict__),
            'wishlist@4862.ch',
            [wish.collection.user.email],
            fail_silently=False,
        )

    context = {"collection": models.Collection.objects.first()}
    # template = loader.get_template('wishlist.html')
    return render(request, "wishlist.html", context)
