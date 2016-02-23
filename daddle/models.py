from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()
    mission = models.ForeignKey('Mission')
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.start_date)

    def active_pledges(self):
        return filter(lambda x: x.is_active(),
                      self.pledge_set.all().order_by('timestamp'))

    def can_start(self):
        return len(self.active_pledges()) >= self.min_people

    def free_slots(self):
        return self.max_people - len(self.active_pledges())

    def is_full(self):
        return self.free_slots() <= 0

    def user_has_active_pledge(self, user):
        for pledge in self.active_pledges():
            if pledge.user == user:
                return True
        return False

@receiver(post_save, sender=Event)
def event_post_save_handler(sender, instance, **kwargs):
    body = """There\'s a new daddle event!

%s - %s
%s
%s

http://daddle.zorzar.de/event/%d""" % (instance.mission.title,
                                       instance.title,
                                       instance.start_date,
                                       instance.description,
                                       instance.id)

    for user in User.objects.all():
        if user.email:
            send_mail('New daddle event!',
                      body,
                      'zz@zoranzaric.de',
                      [user.email],
                      fail_silently=False)


class Pledge(models.Model):
    event = models.ForeignKey('Event')
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    cancel_timestamp = models.DateTimeField(blank=True, null=True)

    def is_active(self):
        return self.cancel_timestamp == None


class Mission(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

