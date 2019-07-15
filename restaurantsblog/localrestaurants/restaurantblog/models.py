from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.db.models import Avg
class category(models.Model):
    name = models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return u"%s" % self.name

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
 
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    category = models.ForeignKey(category,default=3, blank=True, null=True,on_delete=models.CASCADE)
    def averagerating(self):
        Review.objects.filter(restaurant__id=self.id).aggregate(Avg('rating')) 
        #all_ratings = map(lambda x: x.rating, self.review_set.all())
        #return np.mean(all_ratings)
    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    pub_date = models.DateField(default=date.today)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)



