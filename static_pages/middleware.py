from datetime import datetime
from django.http import HttpResponse
# function version

def PrintMessage(get_response):
      def middleware(request):
        response = get_response(request)
        print('welcome ')
        return response
      ## this will back from any view response
      def process_view(request,view_func,view_args,view_kwargs):
        return HttpResponse('welcome')
      # we can handle global exception for errors 
      def process_exception(request,exception):
          return HttpResponse('there was an error')
      
      middleware.process_view = process_view
      middleware.process_exception = process_exception
      return middleware
 

# this is class version
class Timing():
    def __init__(self,get_response):
      self.get_response = get_response
    
    def __call__(self, request) :
       request.current_time=datetime.now()
       response = self.get_response(request)
       print(request.current_time)
       return response