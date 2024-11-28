from django.shortcuts import render
from .models import SliderImage


def index(request):
    slider_images = SliderImage.objects.filter(title='one')
    return render(request, 'index.html', {'slider_images': slider_images})
