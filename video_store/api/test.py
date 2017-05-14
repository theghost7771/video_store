from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token

from .views import UserViewSet
from video_store.video.models import Video


class UserTests(APITestCase):

    def setUp(self):
        self.credentials = {'username': 'user', 'password': 'qweasd'}
        self.user = User.objects.create_user(email='user@…', **self.credentials)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        response = self.client.post('/api/v1/users/')
        self.assertEqual(response.data, {'password': ['This field is required.'],
                                         'username': ['This field is required.']})

        # user creation
        response = self.client.post('/api/v1/users/', data={'username': 'user1', 'password': 'password'})

        self.assertEqual(response.data, {'username': 'user1'})
        self.assertEqual(2, User.objects.count())
        self.assertTrue(User.objects.filter(username='user1').exists())


class VideoTests(APITestCase):

    def setUp(self):
        self.credentials = {'username': 'user', 'password': 'qweasd'}
        self.user = User.objects.create_user(email='user@…', **self.credentials)
        self.client.force_authenticate(user=self.user)

    def test_search_title_rent_and_return(self):
        # without search
        response = self.client.get('/api/v1/videos/')
        # 10 initial titles
        self.assertEqual(len(response.data['results']), 10)

        # searching
        response = self.client.get('/api/v1/videos/?search=title+2')
        self.assertEqual(len(response.data['results']), 1)

        # rental, just add 'rent/' to the entity url
        video_url = response.data['results'][0]['url']
        rental_url = video_url + 'rent/'
        response = self.client.post(rental_url)
        # success rental
        self.assertTrue(response.data['success'])
        # check video is not aviable now
        video = Video.objects.get(title='Title 2')
        self.assertFalse(video.aviable)

        # secondary rental is failed with error
        self.assertEqual(self.client.post(rental_url).data, {"error": "Can't rent not aviable Video."})

        response = self.client.get('/api/v1/videos/?search=title+2')
        video_url = response.data['results'][0]['url']
        # return video, just add 'return/' to the entity url
        return_url = video_url + 'return/'
        response = self.client.post(return_url)
        # success returning
        self.assertTrue(response.data['success'])
        # check video is aviable now
        video = Video.objects.get(title='Title 2')
        self.assertTrue(video.aviable)

        # secondary return is failed with error
        self.assertEqual(self.client.post(return_url).data, {"error": "Can't return not rented Video."})
