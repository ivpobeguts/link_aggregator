import json

from django.test import Client, TestCase
from django.urls import reverse
from links_api.models import Link
from rest_framework import status

client = Client()


class LinksEndpointTest(TestCase):
    """ Test class for posting and getting Links """

    def setUp(self):
        self.valid_url = 'https://www.yahoo.com/'
        self.invalid_url = 'invalid/link'

    def test_create_valid_link(self):
        response = client.post(
            reverse('get_post_links'),
            data=json.dumps({
                'url': self.valid_url
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_link = Link.objects.first()
        self.assertEqual(created_link.url, self.valid_url)

    def test_create_invalid_link(self):
        response = client.post(
            reverse('get_post_links'),
            data=json.dumps({
                'url': self.invalid_url
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['url'][0], 'Enter a valid URL.')

    def test_get_links_sorted_by_score(self):
        link_1 = Link(url=self.valid_url, upvotes=3, downvotes=5)
        link_1.save()
        link_2 = Link(url='https://docs.djangoproject.com/', upvotes=5, downvotes=3)
        link_2.save()
        link_3 = Link(url='https://github.com/', upvotes=5, downvotes=5)
        link_3.save()
        response = client.get(reverse('get_post_links'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['score'], -2)
        self.assertEqual(response.data[1]['score'], 0)
        self.assertEqual(response.data[2]['score'], 2)

    def test_get_links_empty_response(self):
        response = client.get(reverse('get_post_links'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class VoteEndpointsTest(TestCase):
    """ Test class for up- and downvoting for a Link """

    def setUp(self):
        self.link = Link(id=1, url='https://www.yahoo.com/', upvotes=5, downvotes=3)
        self.link.save()

    def test_upvote_link(self):
        response = client.post(
            reverse('upvote_link', kwargs={'link_id': 1}),
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['upvotes'], 6)
        self.assertEqual(response.data['downvotes'], 3)
        self.assertEqual(response.data['score'], 3)

    def test_upvote_link_not_found(self):
        response = client.post(
            reverse('upvote_link', kwargs={'link_id': 10}),
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_downvote_link(self):
        response = client.post(
            reverse('downvote_link', kwargs={'link_id': 1}),
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['upvotes'], 5)
        self.assertEqual(response.data['downvotes'], 4)
        self.assertEqual(response.data['score'], 1)

    def test_downvote_link_not_found(self):
        response = client.post(
            reverse('downvote_link', kwargs={'link_id': 10}),
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
