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

    def get_duration_of_visit(self):
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

    def is_visit_long(self, duration, minutes=60):
        return True if duration.seconds > minutes * 60 else False

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )