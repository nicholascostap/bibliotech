from django.shortcuts import render

def index(request):
    """Redireciona para a página de index."""
    return render(request, 'livro/index.html')
