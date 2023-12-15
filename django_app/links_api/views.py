from datetime import datetime

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from links_api.serializers import LinkOutputSerializer


class LinkView(APIView):

    def post(self, request, link):
        ...

    def get(self, request, *args, **kwargs):
        data = {
            'id': 1,
            'url': 'https://blog.logrocket.com/django-rest-framework-create-api/',
            'upvotes': 0,
            'downvotes': 0,
            'score': 0,
            'created': datetime.now(),
            'updated': datetime.now(),
        }
        serializer = LinkOutputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)