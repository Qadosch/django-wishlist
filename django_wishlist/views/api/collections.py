from ninja import Router
from typing import List
from ninja import ModelSchema

from ...models import Collection


class CollectionSchema(ModelSchema):
    class Config:
        model = Collection
        model_fields = "__all__"


router = Router()

@router.get('/', response=List[CollectionSchema])
def list_collections(request):
    return Collection.objects.all()

@router.get('/{id}', response=CollectionSchema)
def retrieve_collections(request, id):
    return Collection.objects.get(pk=id)


