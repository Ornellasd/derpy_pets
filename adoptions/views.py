from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

@login_required
def new_pet(request):
    if request.method != 'POST':
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.owner = request.user
            new_pet.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'new_pet.html', context)

@login_required
def edit_pet(request, id):
    pet = Pet.objects.get(id=id)

    if pet.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PetForm(instance=pet)
    else:
        form = PetForm(instance=pet, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'pet': pet,'form': form}
    return render(request, 'edit_pet.html', context)

@login_required
def delete_pet(request, id):
    pet = Pet.objects.get(pk=id)
    pet.delete()
    return HttpResponseRedirect(reverse('home'))
