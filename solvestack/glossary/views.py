from rest_framework import viewsets

from .serializers import TermSerializer
from .models import Term
from .filters import TermsFilter


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    filter_class = TermsFilter

