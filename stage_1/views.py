from django.http import HttpResponse, HttpResponseNotFound

# dictionary to return value for the incoming option path
optionValues={"name":"Adonas Haile Mergeta","hobby":"Physical exercise, watching movies","dream":"First, land a job as a python developer, then create a start up"}

# handles the incomeing request if there is no option values get passed from client
def index(response):
   return HttpResponse('Welcome to InternTechHub backend interns stage_1 project')

"""
 handle the request if there is an option from the client.
 if the option matches any of the optionValues keys, the method returns the corresponding value.

"""
def option(response,option):
    if option in optionValues:
      return HttpResponse(optionValues[option])
    else:
      return HttpResponseNotFound('Not Found')
