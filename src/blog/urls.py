from django.urls import path
from .views import BlogHome, BlogCreate, BlogUpdate, BlogDetail, BlogDelete
from django.contrib.auth.decorators import login_required

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='Home'),
    #restreindre l'accès
    # path('create/', login_required(BlogCreate.as_view()), name='create'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('<str:slug>/', BlogDetail.as_view(), name='detail'),
    path('edit/<str:slug>/', BlogUpdate.as_view(), name='edit'),
    path('delete/<str:slug>/', BlogDelete.as_view(), name='delete'),
]