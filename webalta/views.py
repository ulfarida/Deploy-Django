from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mentee, Mentor, Blog

# Create your views here.
def index(request):
    return render(request, 'webalta/index.html', {})

def blog(request):
    blog = Blog.objects.all()
    var_blog = {'blogs' : blog}
    return render(request, 'webalta/blog.html', var_blog)

def mentor(request):
    mentor = Mentor.objects.all()
    var_mentor = {'mentors' : mentor}
    return render(request, 'webalta/mentor.html', var_mentor)

def mentee(request):
    mentee = Mentee.objects.all()
    var_mentee = {'mentees' : mentee}
    return render(request, 'webalta/mentee.html', var_mentee)

def author(request):
    return render(request, 'webalta/author.html', {})

def form(request):
    return render(request, 'webalta/form.html', {})

def blogdetail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    var_blog = {'blog' : blog}
    return render(request, 'webalta/blogdetail.html', var_blog)

def input_blog(request):
    judul = request.POST['judul']
    artikel = request.POST['artikel']
    picture = request.POST['picture']
    tanggal = request.POST['tanggal']

    bloginput = Blog(judul=judul, artikel=artikel, picture=picture, tanggal=tanggal)
    bloginput.save()
    
    blog = Blog.objects.all()
    var_blog = {'blogs' : blog}
    return redirect('blog')
