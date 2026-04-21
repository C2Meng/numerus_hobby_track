from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

#difference of render vs loader.get_template is that render is a shortcut that combines loading the template and rendering it in one step, while loader.get_template only loads the template and returns a Template object that can be rendered later. In this code, we are using render to load the 'test.html' template and then rendering it with an empty context using render() before returning the HttpResponse.
def test(request):
    return render(request, 'test.html')