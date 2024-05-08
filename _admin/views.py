from django.shortcuts import render

# Create your views here.
def admin_page(request):
    context = {
        "text":"this is a text"
    }
    return render(request, 'index.html', context)