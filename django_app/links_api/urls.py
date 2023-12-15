from django.urls import path

from links_api.views import LinkView

urlpatterns = [
    path('/', LinkView.as_view()),
]
