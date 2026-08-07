from django.urls import path
from .views.views import HomeView, LoginView, LogoutView
from .views.friend_views import SearchFriendView

app_name = "chat"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("search-friend/", SearchFriendView.as_view(), name="search_friend"),
    path("add_friend/", SearchFriendView.as_view(), name="add_friend")
]
