from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
from django.db.models import Q



def list (request):
    pet = Pet.objects.all() 
    query = request.GET.get("q")
    if query:
        if query:
            pet = pet.filter(
                Q(name__icontains=query)|
                Q(age__icontains=query)|
                Q(price__icontains=query)
                ).distinct()

    context = {
        "pet" : pet,
    }
    return render(request, 'list.html', context)


def detail (request, pet_id):
    context = {
        "pet" : Pet.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)

def create_pet (request) :
    form = PetForm()
    if request.method == "POST" :
        form = PetForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect ("pet-list")
    context = {
    "form" : form
    }
    return render (request, 'create.html', context)


def update_pet (request, pet_id) :
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST" :
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid() :
            form.save()
            return redirect ('pet-detail', pet_id)
    context = {
    "form" : form,
    "pet_obj" : pet_obj,
    }
    return render (request, 'update.html', context)


def delete_pet (request, pet_id) :
    Pet.objects.get(id=pet_id).delete()
    return redirect ("pet-list")