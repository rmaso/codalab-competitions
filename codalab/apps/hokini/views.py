from django.views.generic import TemplateView

from apps.web.views import HomePageView as CodalabHomePageView


class HomePageView(TemplateView):
    """Template View for homepage."""
    template_name = "hokini/index.html"

class PatrocinadoresView(TemplateView):
    template_name = 'hokini/patrocinadores.html'

class CompeticionesView(CodalabHomePageView):
    """Template View for homepage."""
    template_name = "hokini/competiciones.html"
