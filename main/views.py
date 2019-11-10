from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')


def login(request):
    return render(request, 'login/index.html')


def servers(request):
    return render(request, 'server/index.html')


def switches(request):
    return render(request, 'switch/index.html')


def firewall(request):
    return render(request, 'firewall/index.html')


def routers(request):
    return render(request, 'router/index.html')


def blog_index(request):
    return render(request, 'blog/post/index.html')


