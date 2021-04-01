from rest_framework import serializers
from behavior.models import Behavior, Originator


class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = "__all__"


class OriginatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Originator
        fields = "__all__"
