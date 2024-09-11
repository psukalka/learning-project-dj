from .cms import urls as cms_urls
from django.urls import path, include

from .hotels import Hotels_V1
from . import views

from .streams import HelloClaude_V1

urlpatterns = [
    path("hello-claude/", HelloClaude_V1.as_view()),
    path("ping/", views.ping),
    path("cms/", include(cms_urls)),
    path("hotels/", Hotels_V1.as_view()),
    path("hotels/<int:hotel_id>/", views.index),
    path("hotels/<int:hotel_id>/rooms/", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>", views.index),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/book/", views.index),
    path("users/<int:user_id>/", views.index),
    path("users/<int:user_id>/bookings/", views.index)
]