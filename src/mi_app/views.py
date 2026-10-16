from django.http import HttpResponse
from suma import html_content

def vista_suma(request):
    return HttpResponse(html_content)