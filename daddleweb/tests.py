from django.test import TestCase, Client
from daddle.models import Event, Mission
from django.contrib.auth.models import User

from django.utils import timezone

class ViewTests(TestCase):
    def test_event_can_be_pledged(self):
        User.objects.create_user(username='test', password='test')

        mission = Mission(title='Test Mission')
        mission.save()

        event = Event(title='Test Event',
                      min_people=1,
                      max_people=3,
                      start_date=timezone.now(),
                      mission=mission)
        event.save()

        self.assertEquals(len(event.active_pledges()), 0)

        client = Client()
        self.assertTrue(client.login(username='test', password='test'))

        response = client.post('/pledge', {'event-id': event.id})
        self.assertEquals(response.status_code, 302)

        self.assertEquals(len(event.active_pledges()), 1)

class ViewTests(TestCase):
    def test_pledge_can_be_canceled(self):
        User.objects.create_user(username='test', password='test')

        mission = Mission(title='Test Mission')
        mission.save()

        event = Event(title='Test Event',
                      min_people=1,
                      max_people=3,
                      start_date=timezone.now(),
                      mission=mission)
        event.save()

        self.assertEquals(len(event.active_pledges()), 0)

        client = Client()
        self.assertTrue(client.login(username='test', password='test'))

        response = client.post('/pledge', {'event-id': event.id})
        self.assertEquals(response.status_code, 302)

        self.assertEquals(len(event.active_pledges()), 1)

        response = client.post('/cancel_pledge', {'event-id': event.id})
        self.assertEquals(response.status_code, 302)

        self.assertEquals(len(event.active_pledges()), 0)

