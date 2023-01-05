from django.contrib import admin
from django.urls import path, include
from .views import base1, addWayUser, base2, upvote, unupvote, downvote, undownvote, profile, addcomment, deleteWay, deleteComment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', base1, name="home"),
    path('login/<user>/', base2, name="loggedinHome"),
    path('login/profile/<user>/', profile, name="profile"),

    path('login/addway/<user>/', addWayUser, name="addWayUser"),

    path('login/upvote/<user>/<int:wayId>', upvote, name="like"),
    path('login/unupvote/<user>/<int:wayId>', unupvote, name="unliked"),

    path('login/downvote/<user>/<int:wayId>', downvote, name="dislike"),
    path('login/undownvote/<user>/<int:wayId>', undownvote, name="undisliked"),

    path('login/comment/<user>/<int:wayId>', addcomment, name="addcomment"),

    path('login/deleteWay/<user>/<int:wayId>', deleteWay, name="deleteWay"),
    path('login/deleteComment/<user>/<int:commentId>', deleteComment, name="deleteComment")
]

urlpatterns += staticfiles_urlpatterns()