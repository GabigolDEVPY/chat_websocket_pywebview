from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import RequestFriend, Friend
from .services.friend_service import FriendService



class SearchFriendView(View):
    def get(self, request):
        self.username = request.GET.get("q")
        user = User.objects.filter(username=self.username).exclude(id=request.user.id).first()
        request_friend = RequestFriend.objects.filter(friend=user).first()
        context = {"user": user, "request_friend": request_friend, "is_friend": Friend.objects.filter(user=request.user, friend=user).exists()}
        return render(request, template_name="partials/list_friend_result.html", context=context)
    

class RequestFriendView(View):
    def post(self, request, id):
        self.id = id
        user = User.objects.get(id=id)
        print(user.username)
        if user:
            RequestFriend.objects.bulk_create([
                RequestFriend(user=user, friend=request.user)
                ])
            
        return render(request, template_name="partials/request_pending.html")


class AcceptedFriendView(View):
    def post(self, request, id):
        context = FriendService.accepted_friend(request_id=id, user=request.user)
        return render(request, template_name="partials/requests_list.html", context=context)

