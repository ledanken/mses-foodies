from django.shortcuts import render
from .models import Food

# Create your views here.
def foods(request):
    """views of the foods and delicacies page"""
    
    foods_and_delicacies = Food.objects.all()
    
    context = {
        'foods_and_delicacies': foods_and_delicacies,
    }
    
    return render(request, 'foods/foods.html', context)