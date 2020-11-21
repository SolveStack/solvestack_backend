from rest_framework import serializers

from solvestack.glossary.models import Term


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "definition"]
        read_only_fields = ["id"]
