from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model

from django.conf import settings
from .models import Connection, CONNECTION_STATUS_CONFIRMED, CONNECTION_STATUS_PENDING


@login_required
def profileView(request):
    user = request.user
    return render(request, "profiles/profile_page.html", {"user": user})


@login_required
def profileConnectionView(request):
    user = request.user
    connected_users = Connection.objects.filter(
        user1=request.user, status=CONNECTION_STATUS_CONFIRMED
    )
    pending_users = Connection.objects.filter(
        user1=request.user, status=CONNECTION_STATUS_PENDING
    )
    
    connection_requests = Connection.objects.filter(
        user2=request.user, status=CONNECTION_STATUS_PENDING
    )
    
    return render(request, "profiles/connections_page.html", {
        "user": user,
        "connected_users": connected_users,
        "pending_users": pending_users,
        "connection_requests": connection_requests
        })
    
@login_required
def profileDetail(request, id):
    try:
        user = get_user_model().objects.get(id=id)
        return render(request, "profiles/profile_page.html", {"user": user})

    except:
        return redirect("posts")
    
@login_required
def confirmConnection(request, id):
    try:
        connection =  Connection.objects.get(id=id)
        
        if connection.user2 == request.user:
            connection.status = CONNECTION_STATUS_CONFIRMED
            connection.save()
            
            Connection.objects.create(
                user1 = connection.user2,
                user2 = connection.user1,
                status = CONNECTION_STATUS_CONFIRMED
            )
        
        return redirect("connections")


    except:
    
        return redirect("connections")
    