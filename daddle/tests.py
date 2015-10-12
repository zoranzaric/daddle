from django.test import TestCase
from daddle.models import Event, Pledge
from django.contrib.auth.models import User

from django.utils import timezone

class EventTests(TestCase):
    def test_event_with_min_people_can_start(self):
        user = User()
        user.save()

        event = Event(title='Test Event',
                      min_people=1,
                      max_people=3,
                      start_date=timezone.now())
        event.save()

        pledge = Pledge(event=event, user=user, timestamp=timezone.now())
        pledge.save()

        self.assertTrue(event.can_start())


    def test_empty_event_is_not_full(self):
        event = Event(title='Test Event',
                      min_people=0,
                      max_people=1,
                      start_date=timezone.now())
        event.save()

        self.assertFalse(event.is_full())


    def test_event_with_one_pledge_has_one_active(self):
        user = User()
        user.save()

        event = Event(title='Test Event',
                      min_people=0,
                      max_people=1,
                      start_date=timezone.now())
        event.save()

        pledge = Pledge(event=event, user=user, timestamp=timezone.now())
        pledge.save()

        self.assertEquals(len(event.active_pledges()), 1)


    def test_event_with_one_canceled_pledge_has_no_active(self):
        user = User()
        user.save()

        event = Event(title='Test Event',
                      min_people=0,
                      max_people=1,
                      start_date=timezone.now())
        event.save()

        pledge = Pledge(event=event, user=user,
                        timestamp=timezone.now(),
                        cancel_timestamp=timezone.now())
        pledge.save()

        self.assertEquals(len(event.active_pledges()), 0)


    def test_canceled_pledges_arent_active(self):
        user = User()
        user.save()

        event = Event(title='Test Event',
                      min_people=0,
                      max_people=1,
                      start_date=timezone.now())
        event.save()

        canceled_pledge = Pledge(event=event, user=user,
                        timestamp=timezone.now(),
                        cancel_timestamp=timezone.now())
        canceled_pledge.save()

        pledge = Pledge(event=event, user=user,
                        timestamp=timezone.now())
        pledge.save()

        self.assertEquals(len(event.active_pledges()), 1)
        self.assertEquals(event.active_pledges()[0], pledge)

