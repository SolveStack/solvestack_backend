from rest_framework import serializers

from solvestack.glossary.models import Term, TechnologyNode


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "definition"]
        read_only_fields = ["id"]

class TechnologyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyNode
        fields = ["id", "name", "definition", "similar_tech"]
        read_only_fields = ["id"]