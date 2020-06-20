from django.http import JsonResponse as jr
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getAdvancedStats(req):
    if req.method == 'POST':
        print(req.FILES)
        return jr('Successful')
    return jr('No stats')
