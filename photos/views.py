from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from PIL import Image
import requests



def index(request):
    im = [Image.open("photos/static/images/photo.jpg")]

    return render(request, 'index.html', {'images':im})


