from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'social_site/index.html'
