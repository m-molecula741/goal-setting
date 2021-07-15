from django import forms
from .models import Tag, Book
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    #title = forms.CharField(max_length=50)
    #slug = forms.CharField(max_length=50)

    #title.widget.attrs.update({'class' : 'form-control'})
    #slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Слаг не может быть "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Такой тег уже существует')
        return new_slug

    #def save(self):
    #   new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
    #   return new_tag


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'autor', 'tags', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('слаг не может быть Create')
        if Book.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Книга с подобным слагом существует')
        return new_slug


