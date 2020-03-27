from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for post details
    path('<int:post_id>/', views.detail, name='detail'),
    # Page for listing by categories
    path('categories/', views.categories, name='categories'),
    # Page for listng by specific categories
    path('categories/<int:category_id>/', views.categories, name='categories'),
    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing an existing post
    path('<int:post_id>/edit_post/', views.edit_post, name='edit_post'),
    # Page for adding a new category
    path('new_category/', views.new_category, name='new_category'),
    # Page for editing an existing category
    path(
        'edit_category/<int:category_id>/',
        views.edit_category,
        name='edit_category'
    )
]
