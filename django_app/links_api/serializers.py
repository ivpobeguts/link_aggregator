from rest_framework import serializers

from links_api.models import Link


class LinkOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'created', 'url', 'upvotes', 'downvotes', 'score']


class LinkInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']