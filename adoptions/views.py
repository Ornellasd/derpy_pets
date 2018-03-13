from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

from .models import Pet
from .forms import PetForm

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})

def new_pet(request):
    if request.method != 'POST':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'new_pet.html', context)

def edit_pet(request, id):
    pet = Pet.objects.get(id=id)

    if request.method != 'POST':
        form = PetForm(instance=pet)
    else:
        form = PetForm(instance=pet, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    #context = {'pet': pet,'form': form}
    return render(request, 'edit_pet.html', {'pet': pet, 'form': form})
