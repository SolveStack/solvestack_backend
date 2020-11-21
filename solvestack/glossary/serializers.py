from rest_framework import serializers

from solvestack.glossary.models import Term, Stack


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "definition"]
        read_only_fields = ["id"]


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ["id", "name", "wikipediaLink"]
        read_only_fields = ["id"]

