from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.validators import validate_email
from ninja import Router
from typing import List
from ninja import ModelSchema, Schema
from ninja.errors import ValidationError

from ...models import Wish, Gift


class WishSchema(ModelSchema):
    class Config:
        model = Wish
        model_fields = "__all__"


class GiftSchema(Schema):
    ammount: int = 0
    count: int = 0
    name: str
    email: str
    address: str = ""
    phone: str = ""
    comment: str = ""


router = Router()

@router.get('/', response={200: List[WishSchema]})
def list_wishes(request):
    return Wish.objects.all()


@router.get('/{id}', response={200: WishSchema, 404: Http404})
def retrieve_wish(request, id: int):
    return get_object_or_404(Wish, pk=id)


@router.post('/{id}/gift', response={201: WishSchema, 400: ValidationError, 404: Http404})
def gift_wish(request, id: int, gift: GiftSchema):
    wish = get_object_or_404(Wish, pk=id)

    # validate Material Gift
    if wish.wish_type == wish.MATERIAL:
        if not gift.count > 0:
            raise ValidationError(
                'Missing count field value: %(value)s',
                code='missing',
                params={'value': gift.count},
            )

        if gift.count > wish.missing_count:
            raise ValidationError(
                'Count field value too big: %(value)s',
                code='invalid',
                params={'value': gift.count},
            )

    # validate Material Money Limited Gift
    if wish.wish_type == wish.MONEY_LIMITED:
        if not gift.ammount > 0:
            raise ValidationError(
                'Missing ammount field value: %(value)s',
                code='missing',
                params={'value': gift.ammount},
            )
        if gift.ammount > wish.missing_ammount:
            raise ValidationError(
                'Ammount field value too big: %(value)s',
                code='invalid',
                params={'value': gift.ammount},
            )

    # validate Material Money Unlimited Gift
    if wish.wish_type == wish.MONEY_UNLIMITED:
        if not gift.ammount > 0:
            raise ValidationError(
                'Missing ammount field value: %(value)s',
                code='missing',
                params={'value': gift.ammount},
            )

    # validate email
    if validate_email(gift.email):
        raise ValidationError(
            'Invalid email field value: %(value)s',
            code='invalid',
            params={'value': gift.email},
        )

    return wish.gifts.create(**gift)
