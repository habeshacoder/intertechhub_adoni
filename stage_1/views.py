from django.http import HttpResponse, HttpResponseNotFound


optionValues={"name":"Adonas Haile Mergeta","hobby":"Physical exercise, watching movies","dream":"Landing a job with python developer then develope a start up"}


def index(response):
   return HttpResponse('Welcome to InternTechHub backend interns stage_1 project')
# This method returns an HttpResponse with the value of the option param.
def option(response,option):
    if option in optionValues:
      return HttpResponse(optionValues[option])
    else:
      return HttpResponseNotFound('Not Found')
