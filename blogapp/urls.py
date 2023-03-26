from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, CategoryListView, CategoryDetailView

urlpatterns = [

    
    # ======> class based views URL <======
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
    path('category-detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    

    # ======> class based views URL <======
    # path('blog-list/', views.blog_list, name='blog_list'),
    # path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    
]
