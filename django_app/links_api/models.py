from django.db import models


class Link(models.Model):
    """This class describes the Link model"""

    url = models.URLField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def score(self):
        return self.upvotes - self.downvotes
