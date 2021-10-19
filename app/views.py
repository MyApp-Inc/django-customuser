from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = "app/index.html"


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = '/accounts/login/'