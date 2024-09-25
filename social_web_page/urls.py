from django.contrib import admin
from django.urls import path, include
from register.views import register_view, login_view, logout_view, PerfilUpatadeView, PerfilUsuarioView, follow_user
from feed.views import TweetListView, TweetDeleteView, like_post
from django.conf.urls.static import static
from social_web_page import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('register.urls')),
    path('register/', register_view, name='register'),
    path('perfil/<int:pk>/update/', PerfilUpatadeView.as_view(), name='perfil'),
    path('perfil/<int:pk>/', PerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('seguir/<int:user_id>/', follow_user, name='follow_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('feed/', TweetListView.as_view(), name='feed'),
    path('post/<int:post_id>/delete/', TweetDeleteView.as_view(), name='post_delete'),
    path('like/<int:post_id>/', like_post, name='like_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
