from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path("",views.index, name='home'),
    path("post/<int:pk>",views.postview, name='postview'),
    path("post/<int:pk>/update",views.post_updateview, name='post_updateview'),
    path("post/<int:pk>/delete",views.post_deleteview, name='post_deleteview'),
    path("post/create",views.post_createview, name='post_createview'),
]
