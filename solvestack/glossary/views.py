from rest_framework import viewsets

from solvestack.glossary.serializers import TermSerializer
from solvestack.glossary.models import Term


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer

