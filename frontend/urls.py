from django.urls import path
from .views import IndexView, ArticleDetail


urlpatterns = [
    #path('', AccountView.as_view(), name='account'),
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
]
