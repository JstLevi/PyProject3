from django.shortcuts import render, redirect
from .etl import run_etl
from .models import StudentClean

def upload_and_run(request):
    if request.method == "POST":
        file = request.FILES['csvfile']

        with open("student.csv", "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

        
        run_etl()
        return redirect("success")

    return render(request, "upload.html")

def success(request):
    return render(request, "success.html")
    students = StudentClean.objects.all()
    return render(request, "success.html", {"students": students})

