from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .models import Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMiximin
from .forms import  TagForm, BookForm
from django.urls import reverse
from django.db.models  import Q
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        n = Book.objects.filter(Q(title__icontains=search_query) | Q(autor__icontains=search_query))
    else:
        n = Book.objects.all()
    paginator = Paginator(n, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'books': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'main/index.html', context=context)




def about(request):
    return render(request , 'main/about.html')


def tags_list(request):
    t = Tag.objects.all()
    return render(request, 'main/tags_list.html', context={'tags': t})

class BookDetail(ObjectDetailMixin, View):
    model = Book
    template = 'main/book_detail.html'
    #def get(self, request, slug):
    #  #b = Book.objects.get(slug__iexact=slug)
    #   b = get_object_or_404(Book, slug__iexact=slug)
    # return render(request, 'main/book_detail.html', context={'book': b})"""


"""def book_detail(request, slug):
    b =Book.objects.get(slug__iexact=slug)
    return render(request, 'main/book_detail.html', context={'book': b})"""


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'main/tag_detail.html'
    #def get(self, request, slug):
    #   #t = Tag.objects.get(slug__iexact=slug)
    #  t = get_object_or_404(Tag, slug__iexact=slug)
    #   return render(request, 'main/tag_detail.html', context={'tag': t})"""

"""def tag_detail(request , slug):
    t = Tag.objects.get(slug__iexact=slug)
    return render(request, 'main/tag_detail.html', context={'tag': t})"""


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'main/tag_create.html'
    """def get(self, request):
        f = TagForm()
        return render(request, 'main/tag_create.html', context={'form': f})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, 'main/tag_create.html', context={'form': bound_form})"""


class TagUpdate(ObjectUpdateMiximin,View):
    model = Tag
    model_form = TagForm
    template = 'main/tag_update.html'


class BookUpdate(ObjectUpdateMiximin, View):
    model = Book
    model_form = BookForm
    template = 'main/book_update.html'
    """def get(self, request, slug):
        book = Book.objects.get(slug__iexact=slug)
        bound_form = BookForm(instance=book)
        return render(request, 'main/book_update.html', context={'form': bound_form, 'book': book})

    def post(self, request, slug):
        book = Book.objects.get(slug__iexact=slug)
        bound_form = BookForm(request.POST, instance=book)

        if bound_form.is_valid():
            new_book = bound_form.save()
            return redirect(new_book)
        return render(request, 'main/book_update.html', context={'form': bound_form, 'book': book})"""


class BookCreate(ObjectCreateMixin, View):
    form_model = BookForm
    template = 'main/book_create.html'
    """def get(self, request):
        f = BookForm()
        return render(request, 'main/book_create.html', context={'form': f})

    def post(self, request):
        bound_form = BookForm(request.POST)
        
        if bound_form.is_valid():
            new_book = bound_form.save()
            return redirect(new_book)

        return render(request, 'main/book_create.html', context={'form': bound_form})
"""


class BookDelete(View):
    def get(self, request, slug):
        book = Book.objects.get(slug__iexact=slug)
        return render(request, 'main/book_delete.html', context={'book': book})

    def post(self, request, slug):
        book = Book.objects.get(slug__iexact=slug)
        book.delete()
        return redirect(reverse('main_page'))


class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'main/tag_delete.html', context={'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))


