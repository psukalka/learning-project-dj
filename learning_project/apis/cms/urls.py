from django.urls import path, include

from . import views

urlpatterns = [
    path("hotels/", views.index),
    path("hotels/<int:hotel_id>/", views.index),
    path("hotels/<int:hotel_id>/rooms/", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/bookings/", views.index)
]