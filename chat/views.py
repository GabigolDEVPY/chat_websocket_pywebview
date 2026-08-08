from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["friends"] = self.request.user.friends.all()
        context["friends_requests"] = self.request.user.sent_requests.filter(accepted=False)
        return context
    
    
class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True  


class LogoutView(View):
    def get(self, request, id):
        logout(request)
        return redirect("chat:login")
    
    


        
        
    