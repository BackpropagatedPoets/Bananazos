from django.shortcuts import render

def base(response):
    return render(response, "main/ejemplo_base.html")
