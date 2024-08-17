from .cms import urls as cms_urls
from django.urls import path, include

from . import views

urlpatterns = [
    path("cms/", include(cms_urls)),
    path("hotels/", views.index),
    path("hotels/<int:hotel_id>/", views.index),
    path("hotels/<int:hotel_id>/rooms/", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/book/", views.index),
    path("users/<int:user_id>/", views.index),
    path("users/<int:user_id>/bookings/", views.index)
]