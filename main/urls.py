from django.urls import path
from main import views

urlpatterns = [
    path('', views.blog_home.as_view(), name="blog_home"),
    path('blog/', views.blog.as_view(), name="blog"),
    path('blog_detail/<str:slug>/', views.blog_detail, name="blog_detail"),
    path('contact_us/', views.contactUs.as_view(), name="contact_us"),
    path('services/', views.category.as_view(), name="services"),
    path('about_us/', views.about_us.as_view(), name="about"),
    path('category_detail/<str:slug>/', views.category_detail, name="category_detail"),
    path('videos/', views.videos.as_view(), name="videos"),
    path('gallery/', views.gallery.as_view(), name="gallery"),
   # path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
