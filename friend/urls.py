from django.urls import path
from .views import SearchFriendView, RequestFriendView, AcceptedFriendView

app_name = "friend"

urlpatterns = [
    path("search-friend/", SearchFriendView.as_view(), name="search_friend"),
    path("request_friend/<int:id>", RequestFriendView.as_view(), name="request_friend"),
    path("accepted_friend_request/<int:id>", AcceptedFriendView.as_view(), name="accepted_friend_request")
]
    

