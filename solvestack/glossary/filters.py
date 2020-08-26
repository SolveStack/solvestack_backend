from django_filters import rest_framework as filters

from .models import Term


class TermsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Term
        fields = ("name",)
