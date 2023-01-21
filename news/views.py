from django.shortcuts import render
import random
from .models import New

# Create your views here.

def home(request):
    top_news = New.objects.filter(top_new=True)
    if not top_news:
        top_news = New.objects.all()[:5]
    popular_news = New.objects.all().order_by("-published_at")[:10]
    selected_categories = [
        "Sport",
        "Health",
        "Business",
        "Technology",
        "Entertainment",
        "Politics",
    ]
    top_in_categories = {
        "business": New.objects.filter(category="business")[:3],
        "entertainment": New.objects.filter(category="entertainment")[:2],
        "health": New.objects.filter(category="health")[:4],
        "science": New.objects.filter(category="science")[:2],
        "sports": New.objects.filter(category="sports")[:6],
        "technology": New.objects.filter(category="technology")[:3],
    }
    return render(
        request,
        "index.html",
        {
            "top_news": top_news,
            "popular_news": popular_news,
            "selected_categories": selected_categories,
            "authenticated": True,
            "top_in_categories": top_in_categories,
        },
    )



def view_post(request, pk=None):

    article = New.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'components/article_view.html', context)


def view_categorie(request, pk=None):

    return render(request, 'components/categorie.html')








