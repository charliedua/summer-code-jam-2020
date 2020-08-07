from django.shortcuts import render


# Create your views here.
def homepage(request):
    """ Views to render the homepage. """

    return render(request, "home.html")

def about(request):
    """ Views to render the About Us page. """
    template = "about.html"
    context = about
    return render(request, template)

def error_404_view(request,exception):
    render (request, '404.html')

