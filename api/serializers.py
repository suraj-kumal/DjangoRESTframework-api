from rest_framework import serializers
from base.models import Items


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"
