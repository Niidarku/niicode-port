from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def post_list(request):
    return render(request, 'PersonalPRO/post_list.html')


class AboutView(TemplateView):
    template_name = 'About.html'
