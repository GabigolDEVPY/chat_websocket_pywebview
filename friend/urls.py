from django.urls import path
from .views import SearchFriendView, RequestFriendView

app_name = "friend"

urlpatterns = [
    path("search-friend/", SearchFriendView.as_view(), name="search_friend"),
    path("request_friend/<int:id>", RequestFriendView.as_view(), name="request_friend")
]
    

