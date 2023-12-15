from links_api.models import Link
from rest_framework import serializers


class LinkOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'created', 'url', 'upvotes', 'downvotes', 'score']


class LinkInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']
