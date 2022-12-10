from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.LatestPosts.as_view()),
    path('posts/<slug:category_slug>/<slug:post_slug>/', views.PostDetail.as_view()),
    path('posts/<slug:category_slug>/', views.CategoryDetail.as_view())
]
