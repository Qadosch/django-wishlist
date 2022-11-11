from django.shortcuts import get_object_or_404
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
def retrieve_collection(request, id: int):
    return get_object_or_404(Collection, pk=id)


