from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous():
            return redirect('index')

        return render(request, self.template_name, {'title': 'Вход'})
