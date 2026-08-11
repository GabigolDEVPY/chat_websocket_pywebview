from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from chat.online import ONLINE_USERS



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friends = self.request.user.friends.all()
        for friend in friends:
            friend.is_online = friend.friend.id in ONLINE_USERS
            
        context["friends"] = friends
        context["friends_requests"] = self.request.user.sent_requests.filter(accepted=False)
        return context
    
    
class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True  


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("chat:login")
    
    


        
        
    