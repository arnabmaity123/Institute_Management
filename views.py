from django.shortcuts import render


def home(request):
    return render(request, 'index.html')  # create index.html templates in templates folder
    # and above function redirect to index.html
