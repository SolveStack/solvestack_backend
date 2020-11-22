from rest_framework import serializers

from solvestack.glossary.models import Term, TechnologyNode, Component, Stack


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ["id", "name", "definition"]
        read_only_fields = ["id"]

class TechnologyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyNode
        fields = ["id", "name", "definition",  "wikipedia_link"]
        read_only_fields = ["id"]

class ComponentSerializer(serializers.ModelSerializer):
    technologies = TechnologyNodeSerializer(many=True)
    class Meta:
        model = Component
        fields = ["id", "name", "definition", "wikipedia_link", "technologies"]
        read_only_fields = ["id"]

class StackSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)
    class Meta:
        model = Stack
        fields = ["id", "name", "definition", "wikipedia_link", "components"]
        read_only_fields = ["id"]

