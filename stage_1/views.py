from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

# dictionary to return value based on the  incoming routes
routeValues={"name":"Adonas Haile Mergeta","hobbies":['physical exercise', 'watching movies','coding dailly','listening to music','I love touring but have\'t done one yet'],"dream":"First, land a job as a fullstack developer, then create a startup"}

# handles the incoming request if there is no route values get passed from client
def index(request):
   return HttpResponse('Welcome to InternTechHub backend interns stage_1 project')

# handle the incoming request for /name route
def getName(request):
   return HttpResponse(routeValues["name"])

# handle the incoming request for /hobby route
def getHobby(request):
   return JsonResponse({"hobbies":routeValues["hobbies"]})

# handle the incoming request for /dream route
def getDream(request):
   return HttpResponse(routeValues["dream"])
# handle the incoming request incase there is no valide route
def notFound(request):
   return HttpResponseNotFound()


