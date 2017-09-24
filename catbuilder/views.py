from django.shortcuts import render, get_object_or_404
from .models import Cat
from .forms import CatForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def home(request):
    template = "base.html"
    queryset = Cat.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template, context)

def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cat_detail.html', {'cat': cat})

def new_cat(request):
    if request.method == "POST":
        form = CatForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.date = timezone.now()
            cat.save()
            return redirect('/', pk=cat.pk)
    else:
        form = CatForm()
    return render(request, 'new_cat.html', {'form': form})


def cat_edit(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == "POST":
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            cat.user = request.user
            cat.date = timezone.now()
            return redirect('/', pk=cat.pk)
    else:
        form = CatForm(instance=cat)
    return render(request, 'new_cat.html', {'form': form})



@login_required()
def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    if request.method == 'POST':         # If method is POST,
        cat.delete()                     # delete the cat.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'base.html', {'cat': cat})

@login_required()
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = "profile.html"
    return render(request, template, context)

