from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Review, Restaurant,category
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_restaurants = Restaurant.objects.all().count()
    num_cusines=category.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_restaurants': num_restaurants, 'num_cusines': num_cusines,
                 'num_visits': num_visits},
    )



def restaurant_list(request):
    restaurant_list = Restaurant.objects.order_by('-name')
   
    context = {'restaurant_list':restaurant_list}
    return render(request, 'restaurantblog/restaurant_list.html', context)

def restaurant_category_list(request):
    restaurant_category_list =category.objects.order_by('-name')
   
    context = {'restaurant_category_list':restaurant_category_list}
    return render(request, 'restaurantblog/restaurant_category_list.html', context)    


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    num_restaurantvisits = request.session.get('num_restaurantvisits', 0)
    request.session['num_restaurantvisits'] = num_restaurantvisits+1
    return render(request, 'restaurantblog/restaurant_detail.html', {'restaurant': restaurant},{' num_restaurantvisits': num_restaurantvisits})

def restaurant_category_detail(request,category_id):
  restaurant_category_detail =Restaurant.objects.filter(category= category_id)
 
  return render(request, 'restaurantblog/restaurant_category_detail.html', {'restaurant_category_detail':restaurant_category_detail})






def review_create(request,restaurant_id ):
  restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
  review = Review(
      rating=request.POST.get('rating',False),
      comment=request.POST.get('comment',False),
      user_name=request.POST.get('user_name',False),
     
      restaurant=restaurant)
  review.save()
  return HttpResponseRedirect(reverse('restaurantblog:restaurant_detail', args=(restaurant.id,)))   



