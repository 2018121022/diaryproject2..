from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Diary
from .forms import DiaryForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def cover(request):
    diary_count = Diary.objects.count()
    return render(request, "cover.html", {"diary_count":diary_count})

def index(request):
    diary_index = Diary.objects.all()
    return render(request, "index.html", {"diary_index":diary_index})

def write(request):
    if request.method == "GET":
        return render(request, "write.html")
    
    diary = Diary.objects.create()
    diary.title = request.POST['title']
    diary.body = request.POST['body']
    diary.image = request.FILES['image']
    diary.save()
    return redirect('detail', diary.id)
    

def detail(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    return render(request, "detail.html", {"diary":diary})

def update(request, diary_id):
    if request.method == "GET":
        diary = get_object_or_404(Diary, pk = diary_id)
        return render(request, "update.html", {"diary":diary})

    diary = get_object_or_404(Diary, pk = diary_id)
    title = request.POST['title']
    body = request.POST['body']
    image = request.FILES['image']

    diary.title = title
    diary.body = body
    diary.image = image
    diary.save()
    return redirect('detail', diary.id)

def delete(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    diary.delete()
    return redirect('index')
