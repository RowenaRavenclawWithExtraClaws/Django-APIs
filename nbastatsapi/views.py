from django.http import HttpResponse as hp
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


class MyUploadView(APIView):
    def __init__(self):
        self.parser_class = [FileUploadParser]

    def put(self, req, format=None):
        if 'file' not in req.FILES:
            raise ParseError("Empty content")
        print(req.FILES)


@csrf_exempt
def getAdvancedStats(req):
    if req.method == 'POST':
        print(req.FILES)
        return hp('Successful')
    return hp('No stats')
