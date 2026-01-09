from django.shortcuts import render, redirect
from .models import Restaurant


def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    specialization = request.GET.get('specialization')
    if specialization:
        restaurants = restaurants.filter(
            specialization__icontains=specialization
        )

    return render(request, 'restaurants/list.html', {
        'restaurants': restaurants
    })


def restaurant_form(request, pk=None):
    restaurant = None
    if pk:
        restaurant = Restaurant.objects.filter(id=pk).first()
        if not restaurant:
            return redirect('restaurant_list')

    if request.method == 'POST':
        if restaurant:
            restaurant.name = request.POST.get('name')
            restaurant.specialization = request.POST.get('specialization')
            restaurant.address = request.POST.get('address')
            restaurant.website = request.POST.get('website')
            restaurant.phone = request.POST.get('phone')
            restaurant.save()
        else:
            Restaurant.objects.create(
                name=request.POST.get('name'),
                specialization=request.POST.get('specialization'),
                address=request.POST.get('address'),
                website=request.POST.get('website'),
                phone=request.POST.get('phone'),
            )

        return redirect('restaurant_list')

    return render(request, 'restaurants/form.html', {
        'restaurant': restaurant
    })


def restaurant_delete(request, pk):
    restaurant = Restaurant.objects.filter(id=pk).first()
    if restaurant:
        restaurant.delete()
    return redirect('restaurant_list')
