from django.shortcuts import render, redirect
from .models import Author
from my_app.quotes_app.forms import AuthorForm, QuoteForm


# Create your views here.
def main(request):
    return render(request, 'quotes_app/index.html')

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes_app:main')
        else:
            return render(request, 'quotes_app/author.html', {'form': form})

    return render(request, 'quotes_app/author.html', {'form': AuthorForm()})


def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            # Отримуємо ID автора з форми
            author_id = form.cleaned_data.get('author').id

            # Перенаправляємо на сторінку автора
            return redirect('author_page', author_id=author_id)
        else:
            return render(request, 'quotes_app/quotes.html', {'form': form})
    else:
        form = QuoteForm()
    return render(request, 'quotes_app/quotes.html', {'form': form})