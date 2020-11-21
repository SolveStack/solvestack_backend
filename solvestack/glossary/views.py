from rest_framework import viewsets

from .serializers import TermSerializer, TechnologyNodeSerializer
from .models import Term, TechnologyNode
from .filters import TermsFilter


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    filter_class = TermsFilter

class TechnologyNodeViewSet(viewsets.ModelViewSet):
    queryset = TechnologyNode.objects.all()
    serializer_class = TechnologyNodeSerializer
