from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Room, Message
from django.http import JsonResponse
from django.contrib.auth import logout
from django.shortcuts import redirect



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context
    
    
class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True  


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("chat:login")
    
    


        
        
    