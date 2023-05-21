from django.urls import path
from chat.views import RoomListCreateView, RoomRetrieveUpdateDestroyView

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view(), name='room-retrieve-update-destroy'),
]

