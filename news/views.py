from django.shortcuts import render
from .models import New

# Create your views here.
def home(request):
    top_news = New.objects.filter(top_new=True)
    if not top_news:
        top_news = New.objects.all()[:5]
    top_in_category = New.objects.filter(top_in_category=True)
    popular_news = New.objects.all().order_by("-published_at")[:10]
    selected_categories = [
        "Sport",
        "Health",
        "Business",
        "Technology",
        "Entertainment",
        "Politics",
    ]
    return render(
        request,
        "index.html",
        {
            "top_news": top_news,
            "top_in_category": top_in_category,
            "popular_news": popular_news,
            "selected_categories": selected_categories,
            "authenticated": True,
        },
    )
