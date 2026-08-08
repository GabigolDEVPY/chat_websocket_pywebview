from django.views.generic import TemplateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, response
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import RequestFriend


class SearchFriendView(View):
    def get(self, request):
        self.username = request.GET.get("q")
        user = User.objects.filter(username=self.username).exclude(id=request.user.id).first()
        request_friend = RequestFriend.objects.filter(friend=user).first()
        context = {"user": user, "request_friend": request_friend}
        print(context)
        return render(request, template_name="partials/list_friend_result.html", context=context)
    

class RequestFriendView(View):
    def post(self, request, id):
        self.id = id
        user = User.objects.get(id=id)
        print(user.username)
        if user:
            RequestFriend.objects.create(user=request.user, friend=user)
        return render(request, template_name="partials/request_pending.html")