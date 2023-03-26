from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView

urlpatterns = [

    
    # ======> class based views URL <======
    path('blog-list/', BlogListView.as_view(), name='blog_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),

    # ======> class based views URL <======
    # path('blog-list/', views.blog_list, name='blog_list'),
    # path('blog-detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    
]
