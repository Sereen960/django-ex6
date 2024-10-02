from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from django.http import HttpResponse

def create1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        if not name or not price or not quantity:
            return render(request, 'create.html', {'error': 'All fields except description are required'})

        MyModel.objects.create(name=name, price=price, quantity=quantity, description=description)
        return redirect('readtab')

    return render(request, 'create.html')

def read(request):
    records = MyModel.objects.all()
    return render(request, 'read.html', {'records': records})

def update(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        instance.name = name
        instance.price = price
        instance.quantity = quantity
        instance.description = description
        instance.save()
        return redirect('readtab')

    return render(request, 'update.html', {'instance': instance})

def delete(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('readtab')
    return render(request, 'delete.html', {'record': instance})
