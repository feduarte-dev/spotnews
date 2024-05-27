from django.urls import path
from news.views import home, details, news, CategoryViewSet


urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:news_id>", details, name="news-details-page"),
    path(
        "categories/",
        CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update",
                "delete": "destroy",
            }
        ),
        name="categories-form",
    ),
    path("news/", news, name="news-form"),
]
