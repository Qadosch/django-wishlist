from ninja import Router
from typing import List
from ninja import ModelSchema

from ...models import Wish


class WishSchema(ModelSchema):
    class Config:
        model = Wish
        model_fields = "__all__"


router = Router()

@router.get('/', response=List[WishSchema])
def list_wishes(request):
    return Wish.objects.all()

@router.get('/{id}', response=WishSchema)
def retrieve_wishes(request, id):
    return Wish.objects.get(pk=id)


