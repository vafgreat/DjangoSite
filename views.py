from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    descriptions = Description.objects.all()
    categories = Category.objects.all()

    context = {"descriptions": descriptions, "categories": categories}

    return render(request, "matematika/index.html", context)


def description_page(request, description_id):
    descriptions = Description.objects.all()
    description = get_object_or_404(Description, pk=description_id)
    categories = Category.objects.all()

    context = {"description": description, "descriptions": descriptions, "categories": categories}

    return render(request, "matematika/description.html", context)


