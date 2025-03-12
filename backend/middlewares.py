from rest_framework.request import Request
from rest_framework.response import Response
from backend.settings import SECRET_KEY
from django.http import HttpResponse

class SecretKeyMiddleware:

    def __init__(self, get_respnse):
        self.get_response = get_respnse
    
    def __call__(self, request: Request,*args, **kwds):
        if (not 'admin' in request.build_absolute_uri()) and (not 'schema' in request.build_absolute_uri()):
            try:
                if request.headers['Secret-Key'] == SECRET_KEY:
                    return self.get_response(request)
                return HttpResponse('Permission denied',403)
            except KeyError:
                return HttpResponse('Permission denied',403)
        else:
            return self.get_response(request)