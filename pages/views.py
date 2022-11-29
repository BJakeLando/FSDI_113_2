from django.views.generic import TemplateView
from bs4 import BeautifulSoup
import requests

URL = "https://wttr.in/Sand+Diego" 
HEADERS = {
    "User_Agent": (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    )
}

class HomeView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name='about.html'

class WeatherPageView(TemplateView):
    template_name: "pages/weather.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        response = requests.get(URL, headers = HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            weather_pre = soup.find("pre")
        else:
            weather_pre= "%s" % response.text
        context["weather"] = str(weather_pre)
        return self.render_to_response(context)

