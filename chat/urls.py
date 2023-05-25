from django.urls import path
from chat import views as chat_views
from .views import RoomListCreateView, RoomRetrieveUpdateDestroyView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(), name='room-retrieve-update-destroy'),

    path("", chat_views.chatPage, name='chat-page'),

    # login-section
    path('auth/login/', LoginView.as_view(template_name='LoginPage.html'), name='login-user'),
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),
]

