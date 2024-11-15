from django.http import HttpResponse, HttpResponseNotFound


optionValues={"name":"Adonas Haile Mergeta","hobby":"Physical exercise, watching movies","dream":"Landing a job with python developer then develope a start up"}

# This method returns an HttpResponse with the value of the option param.
def index(response,option):
    if option in optionValues:
      return HttpResponse(optionValues[option])
    else:
      return HttpResponseNotFound('Not Found')