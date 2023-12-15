from django.urls import path

from links_api.views import LinkView, UpvoteView, DownvoteView

urlpatterns = [
    path('', LinkView.as_view(), name='get_post_links'),
    path('<int:link_id>/upvote', UpvoteView.as_view(), name='upvote_link'),
    path('<int:link_id>/downvote', DownvoteView.as_view(), name='downvote_link'),
]
