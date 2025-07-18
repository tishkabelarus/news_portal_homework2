from django.urls import path
from .views import PostsList, PostDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)