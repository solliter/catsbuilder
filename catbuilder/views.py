from django.shortcuts import render, get_object_or_404
from .models import Cat
from .forms import CatForm
from django.shortcuts import redirect


def home(request):
    template = "base.html"
    queryset = Cat.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template, context)


def new_cat(request):
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
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
            return redirect('/', pk=cat.pk)
    else:
        form = CatForm(instance=cat)
    return render(request, 'new_cat.html', {'form': form})


def cat_delete(request, pk):
    cat = get_object_or_404(Cat, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        cat.delete()                     # delete the cat.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'base.html', {'cat': cat})