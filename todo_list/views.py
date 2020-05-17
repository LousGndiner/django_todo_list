from django.shortcuts import render, redirect
from .models import AlumniModel
from .forms import ListAlumni

# Create your views here.
user = 'rjagonzales'
my_name = 'Ray James Amer L. Gonzales'

def home(request):
    return render(request, 'home.html', { 'user': user })

def about(request):
    return render(request, 'about.html', { 'myname': my_name })

def contact(request):
    return render(request, 'contact-us.html', { 'user': user })

def listings(request):
    if request.method == 'POST':
        form = ListAlumni(request.POST or None)
        if form.is_valid():
            form.save()
            all_alumni = AlumniModel.objects.all()
            context = {'all_alumni': all_alumni, 'user': user }
            return render(request, 'listings.html', context)
    else:
        all_alumni = AlumniModel.objects.all()
        context = {'all_alumni': all_alumni, 'user': user}
        return render(request, 'listings.html', context)

def delete(request, alumniModel_id):
    item = AlumniModel.objects.get(pk = alumniModel_id)
    item.delete()
    return redirect('listings')

def view_alumni(request, alumniModel_id):
    alumni = AlumniModel.objects.get(pk = alumniModel_id)
    context = {'alumniModel_id': alumniModel_id, 'alumni': alumni }
    return render(request, 'view_alumni.html', context)

def edit(request, alumniModel_id):
    if request.method == 'POST':
        alumni = AlumniModel.objects.get(pk = alumniModel_id)
        form = ListAlumni(request.POST or None)
        if form.is_valid():
            alumni.lastName = form.cleaned_data.get('lastName')
            alumni.firstName = form.cleaned_data.get('firstName')
            alumni.gender = form.cleaned_data.get('gender')
            alumni.year = form.cleaned_data.get('year')
            alumni.course = form.cleaned_data.get('course')
            alumni.job = form.cleaned_data.get('job')
            alumni.employer = form.cleaned_data.get('employer')
            alumni.save()
            return redirect('listings')
    alumni = AlumniModel.objects.get(pk = alumniModel_id)
    context = {'alumniModel_id': alumniModel_id, 'alumni': alumni }
    return render(request, 'edit.html', context)