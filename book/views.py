from django.core.paginator  import Paginator
from django.views.generic import ListView, DetailView
from .models import Book, Category
from .forms import SearchForm



class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    paginate_by = 2
    queryset = Book.objects.order_by('-created_at')



    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET)
        return context

    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()
        queryset = super().get_queryset()
        category = form.cleaned_data['category']
        if category:
            queryset = queryset.filter(category=category)

        return queryset

        



    


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'

    










