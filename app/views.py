from django.shortcuts import render, redirect
from .form import DailyDiaryForm
from .models import DailyDiary

def frontpage(request):
    diarys = DailyDiary.objects.all()
    return render(request, "frontpage.html", {"diarys": diarys})

def create(request):
    if request.method == "POST":
        form = DailyDiaryForm(request.POST) 
        
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            
            return redirect("frontpage")
    else:
        form = DailyDiaryForm()
    
    return render(request, "createDiary.html", {"form": form})