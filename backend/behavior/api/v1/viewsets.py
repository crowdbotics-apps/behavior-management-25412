from rest_framework import authentication
from behavior.models import Behavior, Originator
from .serializers import BehaviorSerializer, OriginatorSerializer
from rest_framework import viewsets


class BehaviorViewSet(viewsets.ModelViewSet):
    serializer_class = BehaviorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Behavior.objects.all()


class OriginatorViewSet(viewsets.ModelViewSet):
    serializer_class = OriginatorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Originator.objects.all()
