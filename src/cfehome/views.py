import pathlib
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
   return render(request, 'home.html')