from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

def upload_logo(book, filename):
    return "%s/%s" %(book.id, filename)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    face = models.ImageField(upload_to = upload_logo, blank=True, null=True)
    biography = models.TextField(default='biography not available')
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    def get_absolute_url(self):
        return reverse('bookcase:detail_author', kwargs={'pk': self.pk})

    def approve(self):
        self.approved = True
        self.save()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    cover = models.ImageField(upload_to = upload_logo, blank=True, null=True)
    genre = models.CharField(max_length=200, default="unknown")
    add_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='description not available', blank=True, null=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookcase:detail', kwargs={'pk': self.pk})

    def days_since_add(self):
        # calculates day since last add
        now = timezone.now()
        return (now - self.add_date).days

    def approve(self):
        self.approved = True
        self.save()

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
