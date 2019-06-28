import datetime
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if self.leaved_at is None:
            now = timezone.now()
            timedelta_duration = now - self.entered_at
            return timedelta_duration - datetime.timedelta(
                microseconds=timedelta_duration.microseconds
            )
        timedelta_duration = self.leaved_at - self.entered_at
        return timedelta_duration - datetime.timedelta(
            microseconds=timedelta_duration.microseconds
        )

    def is_it_long(self, duration, minutes=60):
        seconds_per_minute = 60
        return duration.seconds > minutes * seconds_per_minute

    def __str__(self):
        username = self.passcard.owner_name
        if self.leaved_at:
            return f'{username} entered at {self.entered_at} {self.leaved_at}'
        return f'{username} entered at {self.entered_at} not leaved'


