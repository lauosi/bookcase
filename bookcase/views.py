from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book, Author, Review
from .forms import BookForm, AuthorForm, ReviewForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect


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

class AddBook(generic.FormView):
    template_name = 'bookcase/add_book.html'
    form_class = BookForm
    success_url =  reverse_lazy('bookcase:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.add_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class AddAuthor(generic.FormView):
    template_name = 'bookcase/add_author.html'
    form_class = AuthorForm
    success_url =  reverse_lazy('bookcase:index')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

class AddReview(generic.FormView):
    template_name = 'bookcase/add_review.html'
    form_class = ReviewForm
    success_url =  reverse_lazy('bookcase:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.book = Book.objects.get(id = self.kwargs['pk'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
