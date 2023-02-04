from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate
from .models import Way, User, Comment
from django.http import HttpResponseRedirect, HttpRequest


# Create your views here.

def base1(req):

    WayList = Way.objects.all().order_by("date")
    comments = Comment.objects.all().order_by("date")

    return render(req, '../templates/base.html', {"way_list": WayList, "user": None, "comments": comments})

def base2(req, user):

    user = req.user
    WayList = Way.objects.all().order_by("date")
    comments = Comment.objects.all().order_by("date")
    return render(req, '../templates/base.html', {"way_list": WayList, "user": user, "comments" : comments})

def profile(req, user):

    samepassword = True
    correctpassword = True

    waysList = Way.objects.all().order_by("date")
    comments = Comment.objects.all().order_by("date")
    user = req.user

    if req.method == 'POST':

        username = req.POST.get('username')
        oldpassword = req.POST.get('password1')
        newpassword = req.POST.get('password2')
        confirmnewpassword = req.POST.get('password3')

        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        profileImg = int(req.POST.get('profileImg'))

        user1 = User.objects.get(pk = user.id)
        user2 = authenticate(req, username = username, password = oldpassword)

        if user2 is not None:

            if newpassword != "" or confirmnewpassword != "":

                if newpassword==confirmnewpassword:

                    user1.set_password(newpassword)
                    user1.first_name = firstname
                    user1.last_name = lastname
                    user1.profileImg = profileImg
                    user1.save()
                    user = user1
        
                else:

                    samepassword = False
                    return render(req, '../templates/profile.html', {"user": user, "samepassword": samepassword, "correctpassword": correctpassword, "waysList": waysList, "comments": comments})
        
            else:

                user1.first_name = firstname
                user1.last_name = lastname
                user1.profileImg = profileImg
                user1.save()
                user = user1
                print(newpassword)

        else:
            correctpassword = False
            return render(req, '../templates/profile.html', {"user": user, "samepassword": samepassword, "correctpassword": correctpassword, "waysList": waysList, "comments": comments})

    return render(req, '../templates/profile.html', {"user": user, "samepassword": samepassword, "correctpassword": correctpassword, "waysList": waysList, "comments": comments})

def addWayUser(req, user):

    date = timezone.now()
    content = req.POST["content"]
    author = req.user

    New_way = Way.objects.create(author = author, content = content, date = date)

    return HttpResponseRedirect(f'/login/{user}')

def upvote(req, user, wayId):

    w = Way.objects.get(pk = wayId)

    if user in w.down():
        down = w.down()
        down.remove(user)
        down = ','.join(down)
        w.downvotes = down

    w.upvotes = w.upvotes + ',' + user
    w.save()

    return HttpResponseRedirect(f'/login/{user}')

def unupvote(req, user, wayId):

    w = Way.objects.get(pk = wayId)
    up = w.up()
    up.remove(user)
    up = ','.join(up)
    w.upvotes = up
    w.save()

    return HttpResponseRedirect(f'/login/{user}')

def downvote(req, user, wayId):

    w = Way.objects.get(pk = wayId)

    if user in w.up():
        up = w.up()
        up.remove(user)
        up = ','.join(up)
        w.upvotes = up

    w.downvotes = w.downvotes + ',' + user
    w.save()

    return HttpResponseRedirect(f'/login/{user}')

def undownvote(req, user, wayId):

    w = Way.objects.get(pk = wayId)
    down = w.down()
    down.remove(user)
    down = ','.join(down)
    w.downvotes = down
    w.save()

    return HttpResponseRedirect(f'/login/{user}')

def addcomment(req, user, wayId):

    date = timezone.now()
    author = req.user
    comment = req.POST.get("comment")

    way = Way.objects.get(pk= wayId)

    new_comment = Comment.objects.create(author = author, comment = comment, way = way, date = date)

    return HttpResponseRedirect(f'/login/{user}')

def deleteWay(req, user, wayId):

    if req.user.is_staff:
        way = Way.objects.get(pk = wayId)
        way.delete()

    else:
        
        way = Way.objects.get(pk=wayId)

        if req.user == way.author:
            way.delete()


    return HttpResponseRedirect(f'/login/{user}')

def deleteComment(req, user, commentId):

    if req.user.is_staff:
        comment = Comment.objects.get(pk=commentId)
        comment.delete()

    else:

        comment = Comment.objects.get(pk=commentId)

        if req.user == comment.author:
            comment.delete()

    return HttpResponseRedirect(f'/login/{user}')
