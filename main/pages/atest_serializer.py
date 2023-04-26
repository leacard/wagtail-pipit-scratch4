from rest_framework import serializers
from wagtail.rich_text import expand_db_html

from .base_serializer import BasePageSerializer
from . import AtestPage


class AtestPageSerializer(BasePageSerializer):
    test_text = serializers.SerializerMethodField()

    class Meta:
        model = AtestPage
        fields = BasePageSerializer.Meta.fields + ["test_text"]

    def get_test_text(self, page):
        return expand_db_html(page.test_text)
