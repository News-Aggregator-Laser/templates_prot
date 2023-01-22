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
        "Sports",
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
            "authenticated": False,
            "top_in_categories": top_in_categories,
        },
    )


def view_post(request, pk=None):
    article = New.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'components/article_view.html', context)


def view_category(request, pk=None):
    return render(request, 'components/categorie.html')


def category(request, category: str):
    category_news = New.objects.filter(category=category.lower())
    selected_categories = [
        "Sports",
        "Health",
        "Business",
        "Technology",
        "Entertainment",
        "Politics",
    ]
    return render(
        request,
        "category_news.html",
        {
            "category": category,
            "category_news": category_news,
            "selected_categories": selected_categories,
            "authenticated": False,
        },
    )
