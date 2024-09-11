from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = 'login.html'


class SignUpPage(TemplateView):
    template_name = 'signup.html'

class AboutUsPage(TemplateView):
    template_name = 'aboutus.html'

