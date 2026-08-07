from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Room, Message
from django.http import JsonResponse, response
from django.contrib.auth.models import User
from django.shortcuts import render


class SearchFriendView(View):
    def get(self, request):
        self.username = request.GET.get("q")
        users = User.objects.filter(username=self.username)
        context = {"users": users}
        return render(request, template_name="partials/list_friends_result.html", context=context)
    

class AddFriendView(View):
    def post(self, request):
        self.id = request.POST.get("id")