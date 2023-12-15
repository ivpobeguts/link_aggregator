from django.urls import path

from links_api.views import LinkView, UpvoteView, DownvoteView

urlpatterns = [
    path('', LinkView.as_view()),
    path('/<int:link_id>/upvote', UpvoteView.as_view()),
    path('/<int:link_id>/downvote', DownvoteView.as_view()),
]
