from django.urls import path

from posts.views import PostlistView, PostDetailView, CommetCreateView

app_name = 'posts'

urlpatterns = [
    path('', PostlistView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommetCreateView.as_view(), name='comment'),
]
