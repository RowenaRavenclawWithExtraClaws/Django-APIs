from django.http import JsonResponse as jr
from django.views.decorators.csrf import csrf_exempt
from .csvHandler import process


@csrf_exempt
def getAdvancedStats(req):
    if req.method == 'POST':
        analytics = process(req.FILES['boxscore'])
        return jr(analytics)
    return jr({"State": "No stats"})
