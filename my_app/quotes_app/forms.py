from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=50, widget=TextInput())
    born_location = CharField(min_length=3, max_length=350, widget=TextInput())
    description = CharField(min_length=3, max_length=5000, widget=TextInput())


    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=3000, required=True, widget=TextInput())
    author = CharField(min_length=3, max_length=150, widget=TextInput())
    tags = CharField(min_length=3, max_length=100, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'tags']
        exclude = ['author']