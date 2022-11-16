from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import HttpResponse,HttpResponseServerError

from .models import Thought, Like
import json

def home(request):
    data = Thought.objects.all().order_by('-updated_at')
    likes = Like.objects.all()
    context = {
        "posts": data,
        "likes": likes
    }
    return render(request, "users/home.html", context=context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def think(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            username = json_data['username']
            message = json_data['message']
            new_thought = Thought()
            new_thought.author = username
            new_thought.message = message
            new_thought.save()
            data = {"username": username, "message": message, "status": "success"}
        except KeyError:
            data = {"status": "none"}
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("Accepts Post Type Only")

def like(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
            try:
                new_like = Like.objects.get(message_id=id)
                like_count = new_like.like_count
                like_count = int(like_count) + 1
                new_like.like_count = like_count
                new_like.save()
            except Exception as e:
                new_like = Like()
                new_like.like_count = 1
                like_count = 1
                new_like.message_id = id
                new_like.save()
            data = {"auto_increment_id": id, "like_count": str(like_count), "status": "success"}
        except KeyError:
            data = {"status": "none"}
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("Accepts Post Type Only")

def delete(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
            Thought.objects.filter(auto_increment_id=id).delete()
            data = {"auto_increment_id": id, "status": "success"}
        except KeyError:
            data = {"status": "none"}
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("Accepts Post Type Only")