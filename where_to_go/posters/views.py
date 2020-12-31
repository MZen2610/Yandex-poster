from django.shortcuts import render

def home(request):
    context = {
    }
    return render(request, template_name='posters/home.html', context=context)