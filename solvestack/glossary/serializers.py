from rest_framework import serializers

from solvestack.glossary.models import Term, StackNode


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "definition"]
        read_only_fields = ["id"]

class StackNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackNode
        fields = ["id", "name", "definition", "similar_tech"]
        read_only_fields = ["id"]