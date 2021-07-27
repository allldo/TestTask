from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'newsBlog'
urlpatterns = [
        path('', views.view, name='news'),
        path('<slug>', views.post, name='post'),
        path('tag/<int:tag_id>', views.tag, name='tag'),
        path('viewsCount/', views.viewsCount, name='listWithViews'),
]