from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Room, Message
from django.http import JsonResponse




class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context
    
    
class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True  




        
        
    