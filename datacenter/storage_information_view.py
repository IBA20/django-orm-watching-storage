from datacenter.models import Visit, format_duration
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True).select_related()
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': f'{format_duration(visit.get_duration())}'
        }
        for visit in visits]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
