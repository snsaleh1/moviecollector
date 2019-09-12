from django.db import models
from django.urls import reverse

# Create your models here.
SNACKS = (
    ('p','With Popcorn'),
    ('c','With Candy'),
    ('i','With Ice Cream'),
    ('c','With Chips'),
    ('s','With Steak')
)

class Movie(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.CharField(max_length=25)
    quote = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class Viewing(models.Model):
    date = models.DateField('Viewing Date')
    snack = models.CharField(
        max_length=50,
        choices=SNACKS,
        default=SNACKS[0][0]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_snack_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']


movies = [
  Movie('American Gangster', '2007', '5/5', 'You can only be two things in this world. Either you somebody, or you nobody'),
  Movie('Gladiator', '2000', '4.5/5', 'Father to a murdered son, husband to a murdered wife, and I will have my vengeance, in this life or the next'),
  Movie('Bad Boys II', '2003', '4.5/5', 'We ride together, we die together, bad boys for life')
]