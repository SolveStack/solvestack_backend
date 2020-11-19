from rest_framework import viewsets

from .serializers import TermSerializer, StackNodeSerializer
from .models import Term, StackNode
from .filters import TermsFilter


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    filter_class = TermsFilter

class StackNodeViewSet(viewsets.ModelViewSet):
    queryset = StackNode.objects.all()
    serializer_class = StackNodeSerializer
