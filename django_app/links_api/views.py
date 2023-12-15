from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from links_api.serializers import LinkOutputSerializer, LinkInputSerializer

from links_api.models import Link


class LinkView(APIView):
    def post(self, request):
        serializer = LinkInputSerializer(data=request.data)
        if serializer.is_valid():
            link_model = Link(url=request.data.get('url'))
            link_model.save()
            return Response(status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        links = Link.objects.all()
        serializer = LinkOutputSerializer(links, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpvoteView(APIView):
    def post(self, request, link_id):
        return _post_vote(link_id=link_id, vote_type="upvotes")


class DownvoteView(APIView):
    def post(self, request, link_id):
        return _post_vote(link_id=link_id, vote_type="downvotes")


def _post_vote(link_id: int, vote_type: str) -> Response:
    link = Link.objects.get(pk=link_id)
    if link:
        setattr(link, vote_type, getattr(link, vote_type) + 1)
        link.save()
        serializer = LinkOutputSerializer(link)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_404_NOT_FOUND)