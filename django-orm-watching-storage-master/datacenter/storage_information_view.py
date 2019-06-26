from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration_of_visit = visit.get_duration_of_visit()
        non_closed_visits.append(
                    {
                        "who_entered": visit.passcard,
                        "entered_at": visit.entered_at,
                        "duration": duration_of_visit,
                        "is_strange": visit.is_visit_long(duration_of_visit)
                    }
                )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
