from django.http import JsonResponse
from django.views import View

from hotels.models import Hotel

class Hotels_V1(View):
    def get(self, request, *args, **kwargs):
        verified_hotels = Hotel.objects.filter(is_active=True)
        response = list()
        for h in verified_hotels:
            response.append(h.to_json())
        return JsonResponse({"items": response})
