from django.urls import path
from .views import HomeView, LoginView, LogoutView
from .views import SearchFriendView

app_name = "friends"

urlpatterns = [
    path("search-friend/", SearchFriendView.as_view(), name="search_friend"),
    path("add_friend/", SearchFriendView.as_view(), name="add_friend")
]
    

