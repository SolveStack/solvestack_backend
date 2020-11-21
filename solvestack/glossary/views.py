from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import TermSerializer, StackSerializer
from .models import Term, Stack
from .filters import TermsFilter


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    filter_class = TermsFilter


class StackViewSet(viewsets.ViewSet):
    queryset = Stack.objects.all()

    def list(self, request):
        serializer = StackSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stack = get_object_or_404(self.queryset, pk=pk)
        serializer = StackSerializer(stack)
        return Response(serializer.data)
