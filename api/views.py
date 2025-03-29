from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Items
from .serializers import ItemSerializer
from rest_framework.exceptions import NotFound


@api_view(["GET"])
def getdata(request):
    items = Items.objects.all()
    allItems = ItemSerializer(items, many=True)
    return Response(allItems.data)


@api_view(["GET"])
def getSingleItem(request, id):
    try:
        item = Items.objects.get(id=id)
        s_item = ItemSerializer(item)
        return Response(s_item.data)

    except Items.DoesNotExist:
        raise NotFound(detail="Item not found")


@api_view(["POST"])
def addItem(request):
    addItem = ItemSerializer(data=request.data)
    if addItem.is_valid():
        addItem.save()
        return Response(addItem.data, status=201)
    return Response(addItem.errors, status=400)


@api_view(["DELETE"])
def deleteItem(request, id):
    try:
        item = Items.objects.get(id=id)
        item.delete()
        return Response("Item deleted")
    except Items.DoesNotExist:
        raise NotFound(detail="Item not found")


@api_view(["PATCH"])
def updateItem(request, id):
    try:
        item = Items.objects.get(id=id)
        updateItem = ItemSerializer(instance=item, data=request.data, partial=True)
        if updateItem.is_valid():
            updateItem.save()
            return Response(updateItem.data, status=201)
        return Response(updateItem.errors, status=404)
    except Items.DoesNotExist:
        raise NotFound(detail="Item not found")


# @api_view(["PUT"])
# def updateItem(request, id):
#     try:
#         item = Items.objects.get(id=id)
#         updateItem = ItemSerializer(instance=item, data=request.data)  # No partial=True
#         if updateItem.is_valid():
#             updateItem.save()
#             return Response(updateItem.data, status=200)
#         return Response(updateItem.errors, status=400)
#     except Items.DoesNotExist:
#         raise NotFound(detail="Item not found")
