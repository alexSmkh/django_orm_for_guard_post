from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard):
        duration_of_visit = visit.get_duration()
        this_passcard_visits.append(
            {
                "entered_at": visit.entered_at,
                "duration": duration_of_visit,
                "is_strange": visit.is_it_long(duration_of_visit)
            }
        )
    context = {
        "passcard": passcode,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
