from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Book, Author

class IndexView(generic.ListView):
    template_name = 'bookcase/index.html'
    context_object_name = 'last_books'

    def get_queryset(self):
        return Book.objects.all().order_by('-add_date')[:3]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        #later change to order by score!
        context['last_add'] = Book.objects.latest('add_date').days_since_add
        context['best_books'] = Book.objects.order_by('title')[:5]
        return context

class DetailView(generic.DetailView):
    model = Book
    template_name = 'bookcase/detail.html'

class DetailAuthor(generic.DetailView):
    model = Author
    template_name = 'bookcase/detail_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailAuthor, self).get_context_data(*args, **kwargs)
        id = self.kwargs['pk']
        author = Author.objects.get(id=id)
        context['authors_books'] = author.book_set.all()
        return context

